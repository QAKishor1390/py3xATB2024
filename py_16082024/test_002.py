import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
...
@pytest.mark.positive
def test_explicit_wait_vwo_login(): #invalid login to check error message
    driver = webdriver.Chrome()

    driver.get("https://app.vwo.com/#/login")
    # Perform actions on the page
    email_input = driver.find_element(By.ID, "login-username")
    pass_input = driver.find_element(By.ID, "login-password")
    email_input.send_keys("admin@gmail.com")
    pass_input.send_keys("admin")
    driver.find_element(By.ID, "js-login-btn").click()

    # A condition to check the element
    #error message comes after 5 seconds
    #Element is visible then assertion
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))




    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
    driver.quit()