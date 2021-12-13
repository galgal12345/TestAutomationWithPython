import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET


class Test_ExternalFiles:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def test_01(self):
        driver.find_element(By.ID, "btn").click()
        time.sleep(5)
        try:
            driver.find_element(By.ID, "checkbox").is_displayed()
        except Exception as e:
            print(e)

    def test_02(self):
        driver.refresh()
        driver.find_element(By.ID, "btn").click()
        time.sleep(5)
        if len(driver.find_elements(By.ID, "checkbox")) > 0:
            print("Element exists on screen")
        else:
            print("Element does NOT exist on screen")

    def teardown_class(cls):
        driver.quit()
