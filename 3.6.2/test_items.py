link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_bascket_button_exists(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket")