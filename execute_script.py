from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputValue = browser.find_element_by_id("input_value").text
    print(inputValue)
    res = calc(int(inputValue))
    print(res)
    area = browser.find_element_by_id("answer")
    area.send_keys(str(res))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
