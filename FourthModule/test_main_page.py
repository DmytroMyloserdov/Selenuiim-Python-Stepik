from .PageObjects.main_page import MainPageObject
from .PageObjects.locators import MainPageObjectLocators

def test_guest_can_go_to_login_page(browser):
    page = MainPageObject(browser, MainPageObjectLocators.PAGE_LINK)
    page.open()
    page.should_be_login_link()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()