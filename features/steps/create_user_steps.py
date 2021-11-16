from json import loads
from behave import *

from features.contexts.create_user_ctx import *
from features.fixtures import fill_form, confirm_message


@given('enter the users page')
def step_impl(context):
    context.browser.find_element_by_xpath(USERS_TAB).click()


@given('click on the add new user button')
def step_impl(context):
    context.browser.find_element_by_xpath(CREATE_USER_BTN).click()


@when('type an username that is already registered')
def step_impl(context):
    fill_form(context, INVALID_USER, VALID_EMAIL)


@when('type an email that is already registered')
def step_impl(context):
    fill_form(context, VALID_USER, INVALID_EMAIL)


@when('type all valid infos')
def step_impl(context):
    fill_form(context, VALID_USER, VALID_EMAIL)


@then('show message saying')
def step_impl(context):
    text_from_step = loads(context.text)
    confirm_message(context, text_from_step['web_ele'], text_from_step['message'])
