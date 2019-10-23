from .base_page import BasePageObject
from .locators import ProductPageObjectLocators, BasePageObjectLocators

class ProductPageObject(BasePageObject):
    def should_be_added_to_basket(self):
        self.should_basket_button_be_presented()
        self.add_to_basket()
        self.should_product_names_be_presented()
        self.should_product_be_added()

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageObjectLocators.BASKET_LINK)
        link.click()
        self.solve_quiz_and_get_code()

    def should_product_names_be_presented(self):
        assert self.is_element_exists(*ProductPageObjectLocators.PRODUCT_NAME), "Product title" + BasePageObjectLocators.NO_ELEMENT_EXCEPTION
        assert self.is_element_exists(*ProductPageObjectLocators.ADDED_PRODUCT), "Added product name" + BasePageObjectLocators.NO_ELEMENT_EXCEPTION

    def should_product_be_added(self):
        title = self.browser.find_element(*ProductPageObjectLocators.PRODUCT_NAME).text
        added_name = self.browser.find_element(*ProductPageObjectLocators.ADDED_PRODUCT).text
        assert title == added_name, "Wrong product added to basket"

    def should_basket_button_be_presented(self):
        assert self.is_element_exists(*ProductPageObjectLocators.BASKET_LINK), "basket button" + BasePageObjectLocators.NO_ELEMENT_EXCEPTION
        