from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePageObject():
    def __init__(self, browser: WebDriver, url: str, timeout = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_exists(self, by_selector: By, selector: str):
        try:
            self.browser.find_element(by_selector, selector)
            return True
        except (NoSuchElementException):
            return False