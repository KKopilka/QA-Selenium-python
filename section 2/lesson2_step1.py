import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
try:
  browser = webdriver.Chrome()
  browser.get(link)
  
  x = browser.find_element_by_id("num1")
  y = browser.find_element_by_id("num2")
  x = x.text
  y = y.text
  c = int(x) + int(y)
 

  select = Select(browser.find_element_by_tag_name("select"))
  select.select_by_value(value=str(c))

  button = browser.find_element_by_css_selector("button.btn")
  button.click()

finally:
  # успеваем скопировать код за 5 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()
