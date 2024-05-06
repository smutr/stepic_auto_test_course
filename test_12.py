from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from sessiun_2.test_3 import calc


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    locator_price = (By.ID, 'price')
    WebDriverWait(browser, 12).until(ES.text_to_be_present_in_element(locator_price, '100'))

    button = browser.find_element(By.ID, 'book')
    button.click()

    x = calc(browser.find_element(By.ID, 'input_value').text)
    time.sleep(1)
    text_input = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', text_input)
    text_input.send_keys(x)
    time.sleep(1)

    button_2 = browser.find_element(By.ID, 'solve')
    button_2.click()

    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
    time.sleep(3)