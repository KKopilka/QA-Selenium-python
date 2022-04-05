from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
class TestAbs(unittest.TestCase):
    def test_link1(self):
        
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element(By.XPATH, '//input[@placeholder="Input your name"]').send_keys("2")
            browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys("fw")
            browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys("hygfyg")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()


            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            assert "Congratulations! You have successfully registered!" == welcome_text