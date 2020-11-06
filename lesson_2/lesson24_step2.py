from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

#browser.get("http://suninjuly.github.io/wait2.html")
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button.click()

x_element = browser.find_element_by_id("input_value")
browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)

button = browser.find_element_by_id('solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(35)

message = browser.find_element_by_id("verify_message")

assert "successful" in message.text