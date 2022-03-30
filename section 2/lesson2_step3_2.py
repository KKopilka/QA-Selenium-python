import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
try:

  browser = webdriver.Chrome()
  browser.get(link)

  button = browser.find_element_by_css_selector("[type='submit']")
  button.click()

  browser.switch_to.window(browser.window_handles[1])

  element = browser.find_element_by_id('input_value')
  x = element.text
  y = calc(x)

  element2 = browser.find_element_by_name('text')
  element2.send_keys(y)

  button2 = browser.find_element_by_css_selector("[type='submit']")
  button2.click()

finally:
  # успеваем скопировать код за 30 секунд
  time.sleep(5)
  # закрываем браузер после всех манипуляций
  browser.quit()