from .base_page import BasePageObject
from .locators import MainPageObjectLocators

class MainPageObject(BasePageObject): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageObjectLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_exists(*MainPageObjectLocators.LOGIN_LINK), "Login link is not presented"