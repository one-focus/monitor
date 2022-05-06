from time import sleep

import telebot
from behave import when
from selenium.webdriver.common.by import By


@when('monitor visa')
def monitor_italian_visa(context):
    all_dates = []
    available_dates_xpath = 'a[not(contains(@class, "appt-table-btn full"))]'
    while True:
        if len(context.driver.find_elements_by_xpath(f'//div[@id="timeTable"]//{available_dates_xpath}')) > 0:
            print('dates found')
            titles = context.driver.find_elements_by_xpath(
                f'//div[@id="timeTable"]//{available_dates_xpath}/preceding-sibling::span[@class="appt-table-d"]')
            titles = [title.text for title in titles]
            for title in titles:
                month = title.split('\n')[0]
                xpath = f'//span[contains(text(),"{month}")]/following-sibling::{available_dates_xpath}'
                times = context.driver.find_elements_by_xpath(xpath)
                all_dates.append([f'{month} : {time.text}' for time in times])
            bot = telebot.TeleBot(context.config['telegram']['telegram_token'])
            bot.send_photo(chat_id=-1001497020962, photo=context.driver.get_screenshot_as_png(),
                           caption=f'{str(all_dates)[:100]}')
        else:
            context.driver.refresh()
            context.current_page.hover_element((By.ID, 'timeTable'))
        sleep(60)


@when('login with "{email}" and "{password}"')
def login_visa(context, email, password):
    context.current_page.click_on('authorize menu')
    context.current_page.click_on('email field')
    context.current_page.type_in('email field', email)
    context.current_page.click_on('password field')
    context.current_page.type_in('password field', password)
    context.current_page.click_on('login button')
    if not context.current_page.is_element_invisible('login button'):
        context.current_page.click_on('authorize menu')
        context.current_page.click_on('email field')
        context.current_page.type_in('email field', email)
        context.current_page.click_on('password field')
        context.current_page.type_in('password field', password)
        context.current_page.click_on('login button')
    sleep(10)
    element = (By.XPATH, '//div[@id="timeTable"]/following-sibling::p/a')
    context.current_page.hover_element(element)
