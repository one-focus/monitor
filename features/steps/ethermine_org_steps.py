from time import sleep

from behave import *
import requests


@when('monitor "{address}" hashrate')
def monitor_hashrate(context, address):
    response = requests.get(f'https://hiveon.net/api/v1/stats/miner/{address.lower}/ETH').json()
    if 'sharesStatusStats' in response or float(response['reportedHashrate']) * 0.000001 < 300:
        context.driver.get(f'https://hiveon.net/eth_ru?miner=0x{address}')
        raise RuntimeError(f"Hash rate is: low")
