from .base_page import BasePageObject
from selenium.webdriver.common.by import By

class MainPageObject(BasePageObject): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_exists(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"