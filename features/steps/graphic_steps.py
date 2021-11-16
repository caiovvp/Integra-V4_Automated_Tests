from behave import *

from features.contexts.graphic_ctx import *
from features.contexts.login_ctx import DASHBOARD_URL

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('time filter is chosen')
def step_impl(context):
    open_period_select(context)
    select_list = context.browser.find_element_by_id('bs-select-2')
    select_options = select_list.find_elements_by_tag_name('li')
    for i in select_options:
        i.click()
        assert_canvas_present(context)
        open_period_select(context)
    open_period_select(context)


@when('integration filter is chosen')
def step_impl(context):
    i = 0
    open_integration_select(context)
    integration_list = context.browser.find_element_by_id('bs-select-1')
    integration_options = integration_list.find_elements_by_tag_name('li')
    for integration in integration_options:
        if i != 0:
            integration = get_integrations(context)[i]
        integration.click()
        context.browser.find_element_by_xpath(GENERATE_GRAPHIC).click()
        if i == 0:
            assert_dashboard_parameter(context, 'A')
        else:
            assert_dashboard_parameter(context, i)
        assert_canvas_present(context)
        open_integration_select(context)
        i += 1
    # open_integration_select(context)


def open_period_select(context):
    context.browser.find_element_by_xpath(PERIOD_FILTER).click()


# @when('integration filter is chosen')
# def validation(context):
#     i = 0
#     for integration in get_integrations(context):
#         open_integration_select(context)
#         if i != 0:
#             integration_list = get_integrations(context)
#             integration = integration_list[i]
#         integration.click()
#         context.browser.find_element_by_xpath(GENERATE_GRAPHIC).click()
#         assert_dashboard_parameter(context, integration)
#         i += 1

def open_integration_select(context):
    context.browser.find_element_by_xpath(INTEGRATION_FILTER).click()


def assert_dashboard_parameter(context, value):
    assert context.browser.current_url == DASHBOARD_URL + f'?process={value}'


#
# def get_integrations(context, integration=0):
#     integration_select = context.browser.find_element_by_name('integration')
#     integration_options = integration_select.find_elements_by_tag_name('option')
#     if integration == 0:
#         return integration_options
#     else:
#         for integra in integration_options:
#             if integra.get_attribute('selected'):
#                 return integra

def get_integrations(context, integration=0):
    integration_list = context.browser.find_element_by_id('bs-select-1')
    integration_options = integration_list.find_elements_by_tag_name('li')
    if integration == 0:
        return integration_options
    else:
        for integra in integration_options:
            if integra.get_attribute('class') == 'selected active':
                return integra


@then('show integrations information of the {div}')
def check_integrations_info(context, div):
    info_div = context.browser.find_element_by_xpath(div)
    info_list = info_div.find_elements_by_tag_name('h3')
    for info in info_list:
        assert info.text != ''


@then('show integrations graphic')
def assert_canvas_present(context):
    # ASSERTS ALL CANVAS ELEMENTS ARE PRESENT AND VISIBLE IN THE PAGE (INCLUDING THE GRAPHIC)
    canvas_list = context.browser.find_elements_by_tag_name('canvas')
    for canvas in canvas_list:
        WebDriverWait(context.browser, 5).until(EC.visibility_of(canvas))
