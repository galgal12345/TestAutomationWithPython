from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium_automation.loudev.support import Support


class Test_LocatorsBasic:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://loudev.com/")

    def test_01(self):
        my_support = Support()
        my_support.verify_elements(driver)

    def teardown_class(cls):
        driver.quit()
