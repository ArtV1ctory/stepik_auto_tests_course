import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    area = browser.find_element_by_id("answer")
    area.send_keys(str(y))
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
