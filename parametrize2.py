import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_feedback_correct(browser, link):
    print(link)
    browser.get(link)
    area = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area.ember-view"))
    )
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    assert feedback.text == 'Correct!', 'Wrong answer!'
