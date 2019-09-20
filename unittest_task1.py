import unittest
from selenium import webdriver
import time


def scenario(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    expected_text = "Congratulations! You have successfully registered!"
    return expected_text, welcome_text


class Unittest(unittest.TestCase):
    def test_link1(self):
        text = scenario("http://suninjuly.github.io/registration1.html")
        expected_text = text[0]
        welcome_text = text[1]
        self.assertEqual(expected_text, welcome_text), \
        'Expected text: {}, real text: {}'.format(expected_text, welcome_text)

    def test_link2(self):
        text = scenario("http://suninjuly.github.io/registration2.html")
        expected_text = text[0]
        welcome_text = text[1]
        self.assertEqual(expected_text, welcome_text), \
        "Expected text: {}, real text: {}".format(expected_text, welcome_text)


if __name__ == "__main__":
    unittest.main()
