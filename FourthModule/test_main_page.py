from .PageObjects.main_page import MainPageObject
from .PageObjects.locators import MainPageObjectLocators, BasePageObjectLocators
from .PageObjects.basket_page import BasketPageObject
from .PageObjects.login_page import LoginPageObject
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPageObject(browser, MainPageObjectLocators.PAGE_LINK)
        page.open()
        page.should_be_login_link()
        login_link = page.go_to_login_page()
        login_page = LoginPageObject(browser, login_link)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link(self, browser):
        page = MainPageObject(browser, MainPageObjectLocators.PAGE_LINK)
        page.open()
        page.is_element_exists(*BasePageObjectLocators.LOGIN_LINK)

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPageObject(browser, MainPageObjectLocators.PAGE_LINK)
    page.open()
    basket_link = page.go_to_basket_page()
    basket = BasketPageObject(page.browser, basket_link)
    basket.should_basket_be_empty()