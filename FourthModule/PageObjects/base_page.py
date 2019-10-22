from selenium.webdriver.chrome.webdriver import WebDriver 

class BasePageObject():
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)