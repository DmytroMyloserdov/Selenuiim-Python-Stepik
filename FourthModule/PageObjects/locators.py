from selenium.webdriver.common.by import By

class BasePageObjectLocators():
    NO_ELEMENT_EXCEPTION = " is not presented"

class MainPageObjectLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageObjectLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")

class ProductPageObjectLocators():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT = (By.CSS_SELECTOR, ".alertinner > strong")