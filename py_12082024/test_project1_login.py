from lib2to3.pgen2 import driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import allure
import allure_result
import allure_pytest





def test_vwo_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()



