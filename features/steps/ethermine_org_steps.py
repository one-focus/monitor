from time import sleep

from behave import *
import requests


@when('monitor "{address}" hashrate')
def monitor_hashrate(context, address):
    address = address.lower()
    response = requests.get(f'https://hiveon.net/api/v1/stats/miner/{address}/ETH').json()
    if float(response['reportedHashrate']) * 0.000001 < 300:
        context.driver.get(f'https://hiveon.net/eth_ru?miner=0x{address}')
        sleep(2)
        context.page_name = f'https://hiveon.net/eth_ru?miner=0x{address}'
        raise RuntimeError(f"Hash rate is: {float(response['reportedHashrate']) * 0.000001}")
