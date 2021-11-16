import time
from json import loads

from selenium.webdriver import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities, Remote

from features.environment_context import *


# FUNCTION THAT INSTANCES THAT THE BROWSER IS CHROME AND THAT IT QUITS ONCE THE TEST IS OVER
def browser_chrome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    capability = DesiredCapabilities.FIREFOX
    context.browser = Remote('http://srv01.connect.com.vc:4444/wd/hub', capability)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


# FUNCTION TO TIMEOUT THE TEST IF NECESSARY
def timeout_for_page_load(context):
    context.browser.set_page_load_timeout(8)


# -- NOTE: Change False for True if you want ipdb debugger running when an error happens
BEHAVE_DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# FILL THE "CREATE NEW USER" FORM
def fill_form(context, user, email):
    context.browser.find_element_by_id('username').send_keys(user)
    context.browser.find_element_by_id('name').send_keys('Nome Sobrenome')
    context.browser.find_element_by_id('email').send_keys(email)
    context.browser.find_element_by_id('active').click()
    context.browser.find_element_by_id('password').send_keys('Senhas@123' + Keys.ENTER)
    time.sleep(1)


# CONFIRM IF MESSAGE IS INSIDE THE TEXT OF A WEB ELEMENT
def confirm_message(context, web_ele, message):
    box = context.browser.find_element_by_xpath(web_ele)
    assert message in box.text


# RETURNS A WEB ELEMENT THAT CONTAINS THE HREF "LINK" IN ITS PROPERTIES
def find_by_link(context, link):
    anchors_list = context.browser.find_elements_by_tag_name('a')
    for element in anchors_list:
        if link in element.get_attribute('href'):
            return element


# RETURNS A LIST OF WEB ELEMENTS FROM THE "UL_OPTIONS" SELECT
def get_list(context):
    list_itens = context.browser.find_element_by_xpath(UL_OPTIONS)
    executions_li = list_itens.find_elements_by_tag_name('li')
    return executions_li


def fill_passwords(context):
    text_from_step = loads(context.text)
    context.browser.find_element_by_id('password').send_keys(text_from_step['password'])
    context.browser.find_element_by_id('confirm').send_keys(text_from_step['password'])


def submit_passwords(context):
    context.browser.find_element_by_id('confirm').send_keys(Keys.ENTER)
    time.sleep(0.5)
    WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "notification-danger")))
