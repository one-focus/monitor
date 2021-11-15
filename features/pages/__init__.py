from .testrail import TestRail

page_map = {
    "testrail": TestRail,
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
