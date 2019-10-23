from .base_page import BasePageObject
from .locators import LoginPageObjectLocators, BasePageObjectLocators

class LoginPageObject(BasePageObject):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Invalid login URL"

    def should_be_login_form(self):
        assert self.is_element_exists(*LoginPageObjectLocators.LOGIN_FORM), "Login form" + BasePageObjectLocators.NO_ELEMENT_EXCEPTION

    def should_be_register_form(self):
        assert self.is_element_exists(*LoginPageObjectLocators.REGISTER_FROM), "Register form" + BasePageObjectLocators.NO_ELEMENT_EXCEPTION

    def register_new_user(self, email, password):
        self.should_be_register_form()
        self.browser.find_element(*LoginPageObjectLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageObjectLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageObjectLocators.REG_CONF_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageObjectLocators.REG_BUTTON).click()