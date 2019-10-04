from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

mainLink = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(mainLink)
    
    inputValue = browser.find_element_by_id("input_value").text

    x = browser.find_element_by_css_selector('input[type="text"]')
    x.send_keys(calc(inputValue))

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkBox = browser.find_element_by_css_selector('input[type="checkbox"]')
    checkBox.click()

    radio = browser.find_element_by_css_selector('input[type="radio"]#robotsRule')
    radio.click()

    button.click()
    time.sleep(10)

finally:
    browser.quit()