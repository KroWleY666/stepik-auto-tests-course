from selenium import webdriver
import time 
import math
import os 

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    #browser.switch_to.window(window_name)
    first_window = browser.window_handles[0]
    browser.get(link)
    

    button = browser.find_element_by_tag_name("button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(35)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла