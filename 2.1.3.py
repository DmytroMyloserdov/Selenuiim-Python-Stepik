from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

mainLink = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(mainLink)
    
    inputValue = browser.find_element_by_id("input_value").text

    x = browser.find_element_by_css_selector('input[type="text"]')
    x.send_keys(calc(inputValue))

    checkBox = browser.find_element_by_css_selector('input[type="checkbox"]')
    checkBox.click()

    radio = browser.find_element_by_css_selector('input[type="radio"]#robotsRule')
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()