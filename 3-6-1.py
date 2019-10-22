from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize(
    'lesson', 
    [
        "236895",
        "236896",
        "236897",
        "236898",
        "236899",
        "236903",
        "236904",
        "236905"
    ]
)
def test_lesson_letter(browser, lesson):
    browser.get(f"https://stepik.org/lesson/{lesson}/step/1")
    browser.find_element_by_css_selector("textarea.textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_css_selector("button.submit-submission  ").click()
    message = browser.find_element_by_class_name("smart-hints__hint").text
    print(message)
    assert message == "Correct!", message