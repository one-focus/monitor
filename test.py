import requests

print(requests.get('https://api.ethermine.org/miner/60575Ec21cEa8432cbd722D64e43026B1C1f72dE/dashboard').json())