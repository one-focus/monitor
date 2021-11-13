from behave import *
import requests


@when('monitor "{address}" hashrate')
def monitor_hashrate(context, address):
    response = requests.get(f'https://api.ethermine.org/miner/{address}/dashboard').json()
    if response['status'] != 'OK' or float(response['data']['statistics'][0]['reportedHashrate']) * 0.000001 < 223:
        context.driver.get(f'https://ethermine.org/miners/{address}/dashboard')
        context.page_name = f'https://ethermine.org/miners/{address}/dashboard'
        raise RuntimeError(f"Hash rate is: {float(response['data']['statistics'][0]['reportedHashrate']) * 0.000001}")
