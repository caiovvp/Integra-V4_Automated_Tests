import time
from json import loads
from behave import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.contexts.change_password_ctx import *
from features.contexts.login_ctx import LOGIN_URL, LOGIN_BTN, DASHBOARD_URL
from features.fixtures import fill_passwords, submit_passwords, find_by_link


@given('user is logged in Integra')
def step_impl(context):
    context.browser.get(LOGIN_URL)
    context.browser.find_element_by_id('username').send_keys('integra_tester')
    context.browser.find_element_by_id('password').send_keys('Senha@123')
    context.browser.find_element_by_xpath(LOGIN_BTN).click()
    assert context.browser.current_url == DASHBOARD_URL


@given('enter the user profile')
def step_impl(context):
    context.browser.find_element_by_xpath(USER_PROFILE).click()


@when('type invalid password')
def step_impl(context):
    fill_passwords(context)
    submit_passwords(context)


@when('type different passwords')
def step_impl(context):
    fill_passwords(context)
    context.browser.find_element_by_id('confirm').send_keys('different')
    submit_passwords(context)


@when('type correct password')
def step_impl(context):
    fill_passwords(context)
    context.browser.find_element_by_id('confirm').send_keys(Keys.ENTER)
    WebDriverWait(context.browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "m-0")))


@then('log out of Integra')
def step_impl(context):
    logout_button = find_by_link(context, '/logout')
    time.sleep(.5)
    webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()
    WebDriverWait(context.browser, 5).until(EC.invisibility_of_element_located((By.CLASS_NAME, "m-0")))
    logout_button.click()


@when('try to log in with the new password')
def step_impl(context):
    text_from_step = loads(context.text)
    for i in range(2):
        context.browser.find_element_by_id('username').send_keys(text_from_step['user'])
        context.browser.find_element_by_id('password').send_keys(text_from_step['password'][i])
        context.browser.find_element_by_xpath(LOGIN_BTN).click()
    assert context.browser.current_url == DASHBOARD_URL
