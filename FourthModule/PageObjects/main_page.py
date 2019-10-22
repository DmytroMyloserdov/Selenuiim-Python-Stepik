from .base_page import BasePageObject
from .login_page import LoginPageObject
from .locators import MainPageObjectLocators

class MainPageObject(BasePageObject): 
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageObjectLocators.LOGIN_LINK)
        link.click()
        return LoginPageObject(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_exists(*MainPageObjectLocators.LOGIN_LINK), "Login link is not presented"