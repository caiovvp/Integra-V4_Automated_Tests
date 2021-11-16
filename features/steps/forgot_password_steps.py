from json import loads
from behave import *

from features.contexts.forgot_password_ctx import *


@given('click on the change password button')
def click_forgot_password(context):
    context.browser.find_element_by_xpath(FORGOT_PASSWORD_BTN).click()


@when('type a valid email on the email box')
def type_valid_email(context):
    context.browser.find_element_by_id("email").send_keys(VALID_EMAIL)


@when('click on the request new password button')
def click_request_password(context):
    context.browser.find_element_by_xpath(REQUEST_PASSWORD_BTN).click()


@then('a message saying that the verification Code was sent is shown')
def new_password_sucess(context):
    context.MESSAGE_BOX = context.browser.find_element_by_xpath(CONFIRMATION_MESSAGE_BOX)
    valid_email_text = loads(context.text)
    assert valid_email_text['msg_valid_email'] in context.MESSAGE_BOX.text


@when('type an invalid email on the email box')
def type_invalid_email(context):
    context.browser.find_element_by_id("email").send_keys(INVALID_EMAIL)


@then('a message saying that no account is linked to that email is shown')
def new_password_fail(context):
    context.MESSAGE_BOX = context.browser.find_element_by_xpath(CONFIRMATION_MESSAGE_BOX)
    invalid_email_text = loads(context.text)
    assert invalid_email_text['msg_invalid_email'] in context.MESSAGE_BOX.text
