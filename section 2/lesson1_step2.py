import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
try:
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element_by_css_selector("[valuex]")
  x = x_element.get_attribute("valuex")
  y = calc(x)

  element1 = browser.find_element_by_id("answer")
  element1.send_keys(y)

  option1 = browser.find_element_by_id("robotCheckbox")
  option1.click()
    
  option2 = browser.find_element_by_id("robotsRule")
  option2.click()

  option3 = browser.find_element_by_css_selector("[type='submit']")
  option3.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()

