from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class Coinmarketcap(BasePage):
    LOGO = By.XPATH, '//img[contains(@src, "https://s2.coinmarketcap.com/static/cloud/img/coinmarketcap_1.svg")]'


    def _verify_page(self):
        self.on_this_page(self.LOGO)
