from pyshould import *
from behave import given, when, then
from capybara.dsl import *
import capybara

capybara.default_max_wait_time = 5
capybara.app_host = "http://localhost:8000"


@given(u'Страница адиминистратора')
def step_impl(context):
    context.saved_table = context.table
    visit("/admin")
    page.fill_in("username", value="admin")
    page.fill_in("password", value="pass")
    page.click_button("Log in")


@then(u'Администратор вводит данные статуса машрута')
def step_impl(context):
    visit("/admin/cargo/routestatus/add/")
    page.fill_in("status", value="load")
    page.click_button("Save")
    visit("/admin/logout")


@then(u'Администратор вводит список водителей')
def step_impl(context):
    for row in context.saved_table:
        visit("/admin/cargo/driver/add/")
        page.fill_in("name", value=row["driver"])
        page.fill_in("phone", value=row["phone"])
        page.click_button("Save")

    visit("/admin/logout")


@given(u'Страница регистрации')
def step_impl(context):
    visit("/acconts/signup/")


@when(u'Оператор вводит учетные записи')
def step_impl(context):
    visit("/acconts/signup/")
    page.fill_in("username", value="user2")
    page.fill_in("password1", value="password")
    page.fill_in("password2", value="password")
    page.click_button("Зарегистрироватся")


@then(u'И переходит на старнницу ввода')
def step_impl(context):
    visit("/")
    assert page.has_title("GARGO"), True


@given(u'Адрес веб страницы')
def step_impl(context):
    visit("/")


@when(u'Оператор открывает страницу')
def step_impl(context):
    context.has_title = page.has_title("GARGO")


@then(u'Тогда видеть титульник')
def step_impl(context):
    assert context.has_title, True


@given(u'Оператор на странице ввода')
def step_impl(context):
    context.saved_table = context.table
    visit("/routes")


@when(u'Опертор ввел данные маршрута')
def step_impl(context):
    visit("/routes")
    for row in context.saved_table:
        visit("/route/create")
        page.select(row['driver_phone'], field="driver")
        page.find("#route").set(row['route'])
        page.find("#gate").set(row['gate'])
        page.select(row['status'], field="status")
        click_button("Сохранить")


@then(u'На странице появляется таблица с данными маршрута c водителем номер телефона')
def step_impl(context):
    for row in context.saved_table:
        assert page.has_text(row['driver']), True
        assert page.has_text(row['phone']), True
        assert page.has_text(row['route']), True
        assert page.has_text(row['status']), True
        assert page.has_text(row['gate']), True


@given(u'Оператор на странице со списком машрутов')
def step_impl(context):
    context.update_table = context.table


@when(u'Оператор переходит по ссылки и вводит корректные данные')
def step_impl(context):
    for row in context.update_table:
        visit("/routes")
        edit_link = "(//td[contains(text(), {})]/parent::tr[1]//span[contains(@class, 'glyphicon-pencil')])[2]"
        page.find('xpath', edit_link.format(row['edit_route'])).click()
        page.find("#route").set(row['correct_route'])
        click_button("Редактировать")


@then(u'На странице со списком машрутов появляется корректный машрут')
def step_impl(context):
    for row in context.update_table:
        assert page.has_text(row['correct_route']), True


@given(u'Оператор удаляет маршрут')
def step_impl(context):
    context.delete_table = context.table
    for row in context.table:
        visit("/routes")
        delete_link = "(//td[contains(text(), {})]/parent::tr[1]//td[contains(@class,'route_delete')]//span[contains(@class,'glyphicon-trash')])[1]"
        page.find('xpath', delete_link.format(row['delete_route'])).click()
        page.click_button("Confirm")


@then(u'На странице со списком машрутов нет удаленного машрута')
def step_impl(context):
    for row in context.delete_table:
        assert not page.has_text(row['delete_route']), True


@when(u'Опертор ввводит данные водителя а затем данные машрута')
def step_impl(context):
    visit("/routes")
    for row in context.saved_table:
        visit("/route/create")
        page.click_link('create_driver')
        page.find("#name").set(row['driver'])
        page.find("#phone").set(row['phone'])
        click_button("Сохранить")
        page.select(row['driver_phone'], field="driver")
        page.find("#route").set(row['route'])
        page.find("#gate").set(row['gate'])
        page.select(row['status'], field="status")
        click_button("Сохранить")


@when(u'Опертор редактирует данные водителя')
def step_impl(context):
    for row in context.update_table:
        visit("/routes")
        edit_link = "(//td[contains(text(), {})]/parent::tr[1]//td[contains(@class,'driver_update')]//span[contains(@class, 'glyphicon-pencil')])[1]"
        page.find('xpath', edit_link.format(row['edit_driver'])).click()
        page.find("#name").set(row['correct_driver'])
        click_button("Редактировать")


@then(u'На странице появляется таблица с обновленными данными водителя')
def step_impl(context):
    for row in context.update_table:
        assert page.has_text(row['correct_driver']), True
