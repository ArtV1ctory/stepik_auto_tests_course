from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    lastname = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    firstname.send_keys("Viki")
    lastname.send_keys("Viki")
    email.send_keys("Viki")

    element = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
