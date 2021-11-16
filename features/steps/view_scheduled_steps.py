from behave import *

from features.contexts.view_executions_ctx import OPEN_LIST_BTN, SHOW_LIST_BTN
from features.contexts.view_scheduled_ctx import *
from features.fixtures import find_by_link, get_list


@when('go to the Schedules tab')
def step_impl(context):
    find_by_link(context, '/integra/schedule/').click()


@when('select a schedule of the list')
def open_list(context):
    context.browser.find_element_by_xpath(OPEN_LIST_BTN).click()


@then('show the list of processes found in that schedule')
def step_impl(context):
    i = 0
    for li in get_list(context):
        if i >= 1:
            open_list(context)
            li = (get_list(context))[i]
        schedule_name = li.find_element_by_class_name('text').text
        li.click()
        context.browser.find_element_by_xpath(SHOW_LIST_BTN).click()
        schedule_title = context.browser.find_element_by_xpath(SCHEDULE_TITLE).text
        assert schedule_name in schedule_title
        i += 1

