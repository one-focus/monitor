from .coinmarketcap import Coinmarketcap
from .italy_visa_page import ItalyVisa
from .testrail import TestRail

page_map = {
    "testrail": TestRail,
    "italy visa": ItalyVisa,
    "coinmarketcap": Coinmarketcap
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
