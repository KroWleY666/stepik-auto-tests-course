from selenium import webdriver
import time 
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def calc(x,y):
  return str(int(x)+int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    #x_checked = x_element.get_attribute("valuex")
    x1 = x.text
    y1 = y.text
    z = calc(x1,y1)
    #print("value of z: ", z)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент с текстом "Python"
    #select.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(35)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла