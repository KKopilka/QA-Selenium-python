import math
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
  browser = webdriver.Chrome()
  browser.get(link)
  
  element1 = browser.find_element_by_name('firstname')
  element1.send_keys("Dori")

  element2 = browser.find_element_by_name('lastname')
  element2.send_keys("MurMur")

  element3 = browser.find_element_by_name('email')
  element3.send_keys("dorimur@yandex.ru")

  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, "file.txt")
  browser.find_element_by_css_selector("#file").send_keys(file_path)

  button = browser.find_element_by_css_selector("[type='submit']")
  button.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()

