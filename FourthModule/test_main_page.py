from .PageObjects.main_page import MainPageObject

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPageObject(browser, link)
    page.open()
    page.go_to_login_page()