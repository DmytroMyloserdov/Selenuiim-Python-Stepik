from selenium.webdriver.common.by import By

class BasePageObjectLocators():
    NO_ELEMENT_EXCEPTION = " is not presented"
    BASKET_PAGE = (By.XPATH, "//*[text()='View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageObjectLocators():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

class LoginPageObjectLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONF_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageObjectLocators():
    PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

class BasketPageObjectLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_NOTE = (By.XPATH, "//*[contains(text(),'Your basket is empty')]")