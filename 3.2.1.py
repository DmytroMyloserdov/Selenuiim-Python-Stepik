import unittest
from selenium import webdriver
import time
import math

def register(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        
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
        return welcome_text_elt.text

    finally:
        browser.quit()

class TestRegistration(unittest.TestCase):
    
    def testRegistrationFirstLink(self):
        self.assertEqual("Congratulations! You have successfully registered!", register("http://suninjuly.github.io/registration1.html"))

    def testRegistrationSecondLink(self):
        self.assertEqual("Congratulations! You have successfully registered!", register("http://suninjuly.github.io/registration2.html"))

if __name__ == "__main__":
    unittest.main()