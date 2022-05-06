from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class ItalyVisa(BasePage):
    MENU_AUTHORIZE = By.XPATH, '//a[@href="login.php"]'
    FIELD_EMAIL = By.ID, 'email'
    FIELD_PASSWORD = By.ID, 'pwd'
    BUTTON_LOGIN = By.ID, 'btn'
    DATE_AVAILABLE = By.XPATH, '//div[@id="timeTable"]//a[contains(@class, "appt-table-btn full")]'

    def _verify_page(self):
        self.on_this_page(self.MENU_AUTHORIZE)
