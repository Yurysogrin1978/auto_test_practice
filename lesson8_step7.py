from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))


    book = browser.find_element_by_id("book")
    book.click()

    x = browser.find_element_by_id('input_value').text
    y = int(x)
    a = math.log(abs(12*math.sin(y)))
    
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(a))

    submit = browser.find_element_by_id("solve")
    submit.click()

    time.sleep(1)
    
    
  
    
finally:
    time.sleep(10)
    browser.quit()
   
