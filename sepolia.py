import logging

import requests
import sys

headers = { 'authority': 'sepoliafaucet.net', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,ru;q=0.8', 'origin': 'https://sepoliafaucet.net', 'referer': 'https://sepoliafaucet.net/', 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"macOS"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
json_data = {'link': sys.argv[1],}
r = response = requests.post('https://sepoliafaucet.net/send_link', headers=headers, json=json_data)
logging.warning(r.text)