from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class TestRail(BasePage):
    FIELD_LOGIN = By.ID, 'name'
    FIELD_PASSWORD = By.ID, 'password'
    BUTTON_LOGIN = By.ID, 'button_primary'
    BUTTON_RUN_AUTOMATED_TESTS = By.ID, 'test_button'
    BUTTON_OK = By.XPATH, '//div[@id="dialog-ident-messageDialog"]//a[contains(@class, "button-ok")]'

    def _verify_page(self):
        self.on_this_page(self.FIELD_LOGIN)
