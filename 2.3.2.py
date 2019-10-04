from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

mainLink = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(mainLink)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    newWindow = browser.window_handles[1]
    browser.switch_to_window(newWindow)

    inputValue = browser.find_element_by_id("input_value").text

    x = browser.find_element_by_css_selector('input[type="text"]')
    x.send_keys(calc(inputValue))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

finally:
    browser.quit()