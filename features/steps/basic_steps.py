from datetime import datetime, timezone, timedelta
from time import sleep

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from telethon import TelegramClient, events

import pages

use_step_matcher('re')


@when('click on (?P<element_name>[^"]*?)(?: in "(?P<section>[^"]*?)")?')
def click_on(context, element_name, section=None):
    sleep(0.5)
    if section:
        section_xpath = context.current_page.get_element_by_name(section)[1]
        element = context.current_page.get_element_by_name(element_name)
        if element[0] == 'xpath':
            try:
                context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}').click()
            except NoSuchElementException:
                raise RuntimeError(f'Не могу кликнуть {element_name} в {section}')
        else:
            raise RuntimeError(f'Используй XPATH для локатора {element_name}')
    else:
        context.current_page.click_on(element_name)


@when('enter "(?P<text>[^"]*)" in (?P<field_name>[^"]*)(?: in "(?P<section>[^"]*?)")?')
def enter_in(context, text, field_name, section=None):
    sleep(0.5)
    if 'generated' in text:
        time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.values[text] = text = text.replace("generated", f'{time.strftime("%d.%m.%Y %H:%M:%S")}')
    if section:
        section_xpath = context.current_page.get_element_by_name(section)[1]
        element = context.current_page.get_element_by_name(field_name)
        if element[0] == 'xpath':
            try:
                element = context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}')
                element.clear()
                element.send_keys(text)
            except NoSuchElementException:
                raise RuntimeError(f'Не могу найти {field_name} в {section}. With xpath {section_xpath}{element[1]}')
        else:
            raise RuntimeError(f'Используй XPATH для локатора {field_name}')
    else:
        context.current_page.type_in(field_name, text)


@then('text "(?P<text>.*)" in (?P<element>.*) is displayed')
def text_in_element_is_state(context, text, element):
    element_text = context.current_page.get_text(element)
    if text not in element_text:
        raise RuntimeError(f'Текст для элемента {element}: "{element_text}". Ожидаемый: {text}')


@then('text "(?P<text>.*)" is displayed')
def text_is_state(context, text):
    element = (By.TAG_NAME, 'body')
    WebDriverWait(context.driver, 10).until(
        ec.text_to_be_present_in_element(element, text), f'Unable to find text: {text}')


@step('page (?P<page_name>.*) is opened')
def init_screen(context, page_name):
    """Instantiating verifies that we're on that page"""
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@step('open url: "(?P<url>.*)"')
def open_url(context, url):
    context.driver.get(url) if url.startswith('http') else context.driver.get(f'https://{url}')


@given('open (?P<page_name>.*) page')
def open_page(context, page_name):
    context.page_name = page_name
    open_url(context, page_name)
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@when('remember (?P<key>.*) as "(?P<value>.*)"')
def remember(context, key, value):
    context.values[value] = context.current_page.get_text(key)


def replace_with_context_values(context, text):
    for value in context.values:
        if value in text:
            text = text.replace(value, context.values[value])
    return text


@when("wait (?P<seconds>.*) sec")
def step_impl(context, seconds):
    sleep(int(seconds))


@when("open last tab")
def step_impl(context):
    context.driver.switch_to_window(context.driver.window_handles[-1])


@when("run monitoring")
def run_monitoring(context):
    # telegram
    client = TelegramClient(
        'any_name',
        context.config['telegram']['api_id'],
        context.config['telegram']['api_hash'])

    @client.on(events.NewMessage(chats=1339855416))
    async def my_event_handler(event):
        save_data(context, event.text)
        print(event.text)

    client.start()
    client.run_until_disconnected()


def save_data(context, text):
    context.time = (datetime.now(timezone.utc) + timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
    context.data_worksheet.insert_rows(values=[[context.time, text]], row=2)
