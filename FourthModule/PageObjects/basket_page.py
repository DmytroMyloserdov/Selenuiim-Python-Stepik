from .base_page import BasePageObject
from .locators import BasketPageObjectLocators

class BasketPageObject(BasePageObject): 
    def should_basket_be_empty(self):
        self.should_no_products_be_apperared()
        self.should_note_be_appeared()

    def should_note_be_appeared(self):
        assert self.is_element_exists(*BasketPageObjectLocators.BASKET_EMPTY_NOTE), "No text of empty basket"

    def should_no_products_be_apperared(self):
        assert self.is_not_element_present(*BasketPageObjectLocators.BASKET_ITEMS), "Not empty product list"