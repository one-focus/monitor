from time import sleep

import telebot
from behave import when
from selenium.webdriver.common.by import By


@when('monitor coins')
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
            context.driver.execute_script("window.scrollTo(0, 255)")
        sleep(60)


@when("get latest coins")
def get_latest_coins(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When get latest coins')