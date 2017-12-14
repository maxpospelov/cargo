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


@when('Опертор ввел данные')
def step_impl(context):
    page.find("#id_new_driver").send_keys("Driver A", Keys.ENTER)


@then('На странице появляется таблица с данными')
def step_impl(context):
    assert page.has_text("Driver A"), True
