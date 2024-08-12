import time

from selenium import webdriver


def test_open_LMSLogin():
    driver=webdriver.Chrome()
    driver.get("https://bjs.dimosh.in/learner/Auth/register")
    driver.maximize_window()
    driver.refresh()
    driver.back()
    print(driver.page_source)
    time.sleep(10)
    driver.quit()
    print("Test Passed")