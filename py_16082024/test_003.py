import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


def test_003_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name= driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys("Kishor Shevkar")
    time.sleep(5)
    driver.quit()
