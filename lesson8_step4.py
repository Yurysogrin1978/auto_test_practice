from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    button.click()


    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = int(x)
    a = math.log(abs(12*math.sin(y)))
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(a))    
    
    button2 = browser.find_element_by_tag_name("button")
    button2.click()

    time.sleep(1)
    
  
    
finally:
    time.sleep(10)
    browser.quit()
   
