import time

from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.contexts.delete_user_ctx import *
from features.contexts.create_user_ctx import USERS_TAB
from features.contexts.login_ctx import LOGIN_BTN


@then('find new user in users page')
def step_impl(context):
    webdriver.ActionChains(context.browser).send_keys(Keys.ESCAPE).perform()
    time.sleep(.5)
    context.browser.find_element_by_xpath(USERS_TAB).click()
    WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((By.NAME, "busca"))) \
        .send_keys('Nome Sobrenome' + Keys.ENTER)
    time.sleep(.5)
    users_box = context.browser.find_element_by_xpath(USERS_BOX)
    assert 'Nome Sobrenome' in users_box.text


@then('delete new user successfully')
def step_impl(context):
    context.browser.find_element_by_xpath(DELETE_USER_BTN).click()
    WebDriverWait(context.browser, 5).until(EC.element_to_be_clickable((By.XPATH, CONFIRM_DELETION)))\
        .click()
    context.browser.find_element_by_class_name('icon-logout').click()


@when('try to log in with deleted user')
def step_impl(context):
    context.browser.find_element_by_id('username').send_keys('new_integra_user')
    context.browser.find_element_by_id('password').send_keys('Senhas@123')
    context.browser.find_element_by_xpath(LOGIN_BTN).click()