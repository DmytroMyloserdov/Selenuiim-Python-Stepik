from .base_page import BasePageObject
from .login_page import LoginPageObject
from .locators import BasePageObjectLocators

class MainPageObject(BasePageObject):
    def should_be_login_link(self):
        assert self.is_element_exists(*BasePageObjectLocators.LOGIN_LINK), "Login link is not presented"