import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    area = browser.find_element_by_id("answer")
    area.send_keys(str(y))
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
