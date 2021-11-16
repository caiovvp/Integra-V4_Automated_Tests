from json import loads
from behave import *

from features.contexts.login_ctx import *


@given('user is on login page')
def step_impl(context):
    context.browser.get(LOGIN_URL)
    assert context.browser.current_url == LOGIN_URL


@when('type credentials')
def step_impl(context):
    text_from_step = loads(context.text)
    for i in range(len(text_from_step["user"])):
        context.browser.find_element_by_id('username').send_keys(text_from_step["user"][i])
        context.browser.find_element_by_id('password').send_keys(text_from_step["password"][i])
        context.browser.find_element_by_xpath(LOGIN_BTN).click()


@then('the dashboard page should open')
def step_impl(context):
    assert context.browser.current_url == DASHBOARD_URL
