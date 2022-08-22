from time import sleep

from behave import *
import requests


@when('monitor "{address}" hashrate')
def monitor_hashrate(context, address):
    context.driver.get(f'https://hiveon.net/eth_ru?miner=0x{address}')
    text = context.driver.find_element_by_xpath('//div[text()="В реальном времени"]/..//span[1]').text
    if float(text) < 270:
        sleep(5)
        raise RuntimeError(f"Hash rate is: {text}, expected 270+")
