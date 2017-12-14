from pyshould import *
from behave import given, when, then
from capybara.dsl import *
from selenium.webdriver.common.keys import Keys
import time


URL_PROJECT = 'http://localhost:8000'


@given('Адрес веб страницы')
def step_impl(context):
    visit(URL_PROJECT)


@when('Оператор открывает страницу')
def step_impl(context):
    context.has_title = page.has_title("GARGO")


@then('Тогда видеть титульник')
def step_impl(context):
    assert context.has_title, True


@given('Оператор на странице ввода')
def step_impl(context):
    visit(URL_PROJECT)


@when('Опертор ввел данные маршрута с водителем {drivers}')
def step_impl(context, drivers):
    for driver in drivers:
        page.find("#id_new_driver").send_keys(drivers, Keys.ENTER)


@then('На странице появляется таблица с данными маршрута c водителем {drivers_on_page}')
def step_impl(context, drivers_on_page):
    for driver in drivers_on_page:
        assert page.has_text(driver), True
