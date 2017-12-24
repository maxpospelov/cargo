from pyshould import *
from behave import given, when, then
from capybara.dsl import *
import capybara

capybara.default_max_wait_time = 5
capybara.app_host = "http://localhost:8000"


@given('Адрес веб страницы')
def step_impl(context):
    visit("/")


@when('Оператор открывает страницу')
def step_impl(context):
    context.has_title = page.has_title("GARGO")


@then('Тогда видеть титульник')
def step_impl(context):
    assert context.has_title, True


@given('Оператор на странице ввода')
def step_impl(context):
    context.saved_table = context.table
    for row in context.table:
        visit("/route/create")
        page.find("#id_driver").set(row['driver'])
        page.find("#id_phone").set(row['phone'])
        page.find("#id_route").set(row['route'])
        click_button("Save")


@when('Опертор ввел данные маршрута  с водителем  и номер телефона водителя')
def step_impl(context):
    visit("/routes")


@then('На странице появляется таблица с данными маршрута c водителем номер телефона')
def step_impl(context):
    for row in context.saved_table:
        assert page.has_text(row['driver']), True
        assert page.has_text(row['phone']), True
        assert page.has_text(row['route']), True


@given('Оператор на странице со списком машрутов')
def step_impl(context):
    context.update_table = context.table
    for row in context.table:
        visit("/routes")
        edit_link = "(//td[contains(text(), {})]/parent::tr[1]//a[contains(text(),'Edit')])[1]"
        page.find('xpath', edit_link.format(row['edit_route'])).click()
        page.find("#id_route").set(row['correct_route'])
        click_button("Update")


@when(u'Оператор переходит по ссылки и вводит корректные данные')
def step_impl(context):
    visit("/routes")


@then(u'На странице со списком машрутов появляется корректный машрут')
def step_impl(context):
    for row in context.update_table:
        assert page.has_text(row['correct_route']), True


@given(u'Оператор удаляет маршрут')
def step_impl(context):
    context.delete_table = context.table
    for row in context.table:
        visit("/routes")
        delete_link = "(//td[contains(text(), {})]/parent::tr[1]//a[contains(text(),'Delete')])[1]"
        page.find('xpath', delete_link.format(row['delete_route'])).click()
        page.click_button("Confirm")


@then(u'На странице со списком машрутов нет удаленного машрута')
def step_impl(context):
    for row in context.delete_table:
        assert not page.has_text(row['delete_route']), True
