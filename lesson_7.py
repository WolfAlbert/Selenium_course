from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import math 

fake = Faker()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    ChromeDriverManager().install
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, 'input_value').text

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(calc(x))

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()