# ********** Selenium Concepts : Waits ***********
# don't use time.sleep'
# Types of waits
# 1. Implicit wait : We don't use this wait, because it is global wait
# 2. Explicit wait
# 3. Fluent wait
# 4. Thread sleep
# 5. Custom wait
# 6. Wait for page load
# 7. Wait for element to be visible
# 8. Wait for element to be clickable
import time

# WAP of implicit wait

import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

...
@pytest.mark.positive
def test_implicit_wait_vwo_login(): #invalid login to check error message
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # seconds
    driver.get("https://app.vwo.com/#/login")
    # Perform actions on the page
    email_input = driver.find_element(By.ID, "login-username")
    pass_input = driver.find_element(By.ID, "login-password")
    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")
    driver.find_element(By.ID, "js-login-btn").click()
    time.sleep(5)
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()
