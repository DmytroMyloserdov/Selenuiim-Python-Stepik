from selenium import webdriver
import time
import math

mainLink = "http://suninjuly.github.io/registration1.html"
# mainLink = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(mainLink)
    
    requiredDiv = browser.find_element_by_class_name("first_block")
    
    firstName = requiredDiv.find_element_by_class_name("first")
    lastName = requiredDiv.find_element_by_class_name("second")
    email = requiredDiv.find_element_by_class_name("third")

    firstName.send_keys("a")
    lastName.send_keys("a")
    email.send_keys("a")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()