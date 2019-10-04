from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "a.txt")

    browser.find_element_by_name("firstname").send_keys("a")
    browser.find_element_by_name("lastname").send_keys("a")
    browser.find_element_by_name("email").send_keys("a")
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()