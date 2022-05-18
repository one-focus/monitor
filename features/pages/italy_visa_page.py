from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class ItalyVisa(BasePage):
    MENU_AUTHORIZE = By.XPATH, '//a[@href="login.php"]'
    FIELD_EMAIL = By.ID, 'email'
    FIELD_PASSWORD = By.ID, 'pwd'
    BUTTON_LOGIN = By.ID, 'btn'
    DATE_AVAILABLE = By.XPATH, '//div[@id="timeTable"]//a[contains(@class, "appt-table-btn full")]'

    BUTTON_CREATE_APPLICATION = By.XPATH, '//input[@type="button" and contains(@class, "important")]'

    FIELD_SURNAME = By.ID, 'f_pers_surnames'
    FIELD_FIRST_NAME = By.ID, 'f_pers_givennames'
    FIELD_LOCAL_NAME = By.ID, 'f_pers_local_name'
    CHECKBOX_SEX_MALE = By.ID, 'f_pers_sex-M'
    CHECKBOX_SEX_FEMALE = By.ID, 'f_pers_sex-F'
    FIELD_DOB = By.ID, 'f_pers_birth_date'
    FIELD_DOCUMENT_NUMBER = By.ID, 'f_pass_num'
    FIELD_ISSUE_DATE = By.ID, 'fi_passport_issue_date'
    FIELD_EXPIRE_DATE = By.ID, 'fi_passport_expiry_date'
    DROPDOWN_OCCUPATION_STATUS = By.ID, 'f_pers_occupation'
    DROPDOWN_MARITAL_STATUS = By.ID, 'f_fami_marital_status'
    FIELD_MOBILE_NUMBER = By.ID, 'f_pers_mobile_phone'

    DROPDOWN_DESTINATION = By.ID, 'fi_trav_main_dest'
    FIELD_ARIVAL_DATE = By.ID, 'f_trav_departure_date'
    FIELD_DEPARTURE_DATE = By.ID, 'f_trav_arrival_date'

    FIELD_INSURANCE_START_DATE = By.ID, 'f_trav_insurance_begin_date'
    FIELD_INSURANCE_END_DATE = By.ID, 'f_trav_insurance_end_date'

    CHECKBOX_DELIVERY_YES = By.ID, 'fi_passback_service-t'
    CHECKBOX_DELIVERY_NO = By.ID, 'fi_passback_service-f'

    FIELD_HOME_NUMBER = By.ID, 'fi_passback_address'
    FIELD_STREET = By.ID, 'fi_passback_address'
    FIELD_CITY = By.ID, 'fi_passback_address'
    FIELD_POSTCODE = By.ID, 'fi_passback_address'

    BUTTON_SAVE = By.ID, 'save_button'

    def _verify_page(self):
        self.on_this_page(self.MENU_AUTHORIZE)
