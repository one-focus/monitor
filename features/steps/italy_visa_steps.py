from time import sleep

import telebot
from behave import when
from selenium.webdriver.common.by import By


@when('monitor visa')
def monitor_italian_visa(context):
    all_dates = []
    available_dates_xpath = 'a[not(contains(@class, "appt-table-btn full"))]'
    while True:
        if context.current_page.is_element_displayed('create application button'):
            bot = telebot.TeleBot(context.config['telegram']['telegram_token'])
            bot.send_photo(chat_id=-1001497020962, photo=context.driver.get_screenshot_as_png(),
                           caption=f'Слетели данные')
        elif len(context.driver.find_elements_by_xpath(f'//div[@id="timeTable"]//{available_dates_xpath}')) > 0:
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
            if len(context.driver.find_elements_by_class_name('form_status')) > 0:
                context.current_page.hover_element((By.CLASS_NAME, 'form_status'))
            else:
                login_visa(context)
        sleep(3600)


def fill_form(context, json):
    json = {
        'surname': '',
        'first_name': '',
        'sex': '',
        'dob': '',
        'country_of_birth': '',
        'nationality': '',
        'type_of_document': '',
        'document_number': '',
        'issue_date': '',
        'expiry_date': '',
        'issued_by': '',
        'occupation_status': '',
        'marital_status': '',
        'mobile_number': '',
        'main_destination': '',
        'date_of_arrival_schengen': '',
        'date_of_departure_schengen': '',
        'insurance_start_date': '',
        'insurance_end_date': '',
        'passport_delivery': '',
        'home_number': '',
        'street': '',
        'city': '',
        'postcode': '',
    }


@when('login visa')
def login_visa(context):
    logins = {'priva898@mail.ru': 'Viza2020!', 'nina.minsk@bk.ru': 'Vl6689563*', 'kauha1978@mail.ru': 'Viza2020!',
              'ida1516@mail.ru': 'Viza2020!', 'mikha160783@mail.ru': 'Viza2020!', 'veko1717@mail.ru': 'Viza2020!',
              'veko1616@mail.ru': 'Viza2020!', 'kovalok1919@mail.ru': 'Viza2020!', 'halinam1963@mail.ru': 'Viza2020!',
              'viktar1959@mail.ru': 'Viza2020!', 'bezmenv1982@mail.ru': 'Viza2020!',
              'aleks_ber88@mail.ru': 'Vl6689563*', 'masha.list66@mail.ru': 'Vl6689563*',
              'vadim77by@yandex.ru': 'Vl6689563*', 'romanukyur71@gmail.com': 'Vl6689563*'}
    messages = (By.XPATH,
                '//*[contains(text(),"Your account is temporarily locked") or contains(text(), "Please enter the provided e-mail address")]')
    for email, password in logins.items():
        login(context, email, password)
        sleep(10)
        if context.current_page.is_element_displayed(messages):
            continue
        if not context.current_page.is_element_invisible('login button'):
            login(context, email, password)
            sleep(10)
            if not context.current_page.is_element_invisible('login button'):
                break
        else:
            break
    else:
        raise RuntimeError(f'Unable to login. Error is {context.current_page.get_text(messages)}')
    context.driver.execute_script("window.scrollTo(0, 500)")


def login(context, email, password):
    context.current_page.click_on('authorize menu')
    context.current_page.click_on('email field')
    context.current_page.type_in('email field', email)
    context.current_page.click_on('password field')
    context.current_page.type_in('password field', password)
    context.current_page.click_on('login button')
