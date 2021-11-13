from .google_page import GooglePage

page_map = {
    "google.com": GooglePage,
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
