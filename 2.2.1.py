from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    number = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
    browser.find_element_by_tag_name("select").find_element_by_css_selector('[value = "' + str(number) + '"]').click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
