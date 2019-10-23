from .PageObjects.product_page import ProductPageObject
from .PageObjects.locators import ProductPageObjectLocators
from .PageObjects.basket_page import BasketPageObject
import pytest

@pytest.mark.parametrize(
    'link', 
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks = pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ]
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPageObject(browser, link)
    page.open()
    page.should_be_added_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPageObject(browser, ProductPageObjectLocators.PAGE_LINK)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageObjectLocators.SUCCESS_ALERT)

def test_guest_cant_see_success_message(browser):
    page = ProductPageObject(browser, ProductPageObjectLocators.PAGE_LINK)
    page.open()
    assert page.is_not_element_present(*ProductPageObjectLocators.SUCCESS_ALERT)

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPageObject(browser, ProductPageObjectLocators.PAGE_LINK)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageObjectLocators.SUCCESS_ALERT)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPageObject(browser, ProductPageObjectLocators.PAGE_LINK)
    page.open()
    basket_link = page.go_to_basket_page()
    basket = BasketPageObject(page.browser, basket_link)
    basket.should_basket_be_empty()