from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    res = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(res))
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
