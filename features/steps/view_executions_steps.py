from behave import *

from features.contexts.view_executions_ctx import *
from features.fixtures import find_by_link, get_list


@given('go to the Executions tab')
def step_impl(context):
    find_by_link(context, '/integra/execucoes').click()


@when('go to all processes')
def step_impl(context):
    context.browser.find_element_by_xpath(ALL_PROCESSES).click()


@then('show the all the executions of all processes')
def step_impl(context):
    process_title = context.browser.find_element_by_xpath(PROCESS_TITLE)
    assert process_title.text == 'Todos as execuções do processo'
    executions_length = get_executions_length(context)
    assert executions_length == 10


@when('choose a filter')
def step_impl(context):
    open_select = context.browser.find_element_by_xpath(FILTER_BTN)
    open_select.click()
    select_list = context.browser.find_element_by_id('bs-select-1')
    select_options = select_list.find_elements_by_tag_name('li')
    all_length = get_executions_length(context)
    max_length = all_length * 2
    for i in select_options:
        i.click()
        executions_length = get_executions_length(context)
        max_length -= executions_length
        open_select.click()
    assert max_length == 0


@then('show only processes according with that filter')
def get_executions_length(context):
    executions_div = context.browser.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div')
    executions_empty = executions_div.find_elements_by_class_name('d-none')
    executions_length = 10 - len(executions_empty)
    return executions_length


@when('select a process of the list')
def open_list(context):
    context.browser.find_element_by_xpath(OPEN_LIST_BTN).click()


@then('show a list of all executions on that process')
def step_impl(context):
    i = 0
    for li in get_list(context):
        if i >= 1:
            open_list(context)
            li = (get_list(context))[i]
        execution_name = li.find_element_by_class_name('text').text
        li.click()
        context.browser.find_element_by_xpath(SHOW_LIST_BTN).click()
        execution_title = context.browser.find_element_by_xpath(EXECUTION_TITLE).text
        assert execution_name in execution_title
        i += 1