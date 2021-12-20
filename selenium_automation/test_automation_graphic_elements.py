import time

import allure
import pytest
import softest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

eyes = Eyes()


class Test_AutomationGraphicElements:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://applitools.com/helloworld/")
        driver.implicitly_wait(1)
        eyes.api_key = 't7WFF9UtEZ7wXj5WccoKQu03VHVkRod98SyAeJAFaQY0110'

    def test_01(self):
        eyes.open(driver, "test_01", "Blh Blh Industry")
        eyes.check_window('My First Screen Shot 😄')
        driver.find_element(By.LINK_TEXT, "?diff1").click()
        eyes.check_window("clicking diff1")
        driver.find_element(By.LINK_TEXT, "?diff2").click()
        eyes.check_window("clicking diff2")
        driver.find_element(By.TAG_NAME, "button").click()
        eyes.check_window("clicking button")

    def teardown_class(cls):
        eyes.close()
        driver.quit()
        eyes.abort()
