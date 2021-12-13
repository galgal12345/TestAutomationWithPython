from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Test_SuperClacVerOne:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://juliemr.github.io/protractor-demo/")

    def test_01(self):
        operator = Select(driver.find_element(By.CSS_SELECTOR, " form select"))
        operator.select_by_visible_text("*")

        for j in range(1, 4):
            for i in range(1, 4):
                right_field = str(j)
                left_field = str(i)
                driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").send_keys(right_field)
                driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys(left_field)
                driver.find_element(By.ID, "gobutton").click()
                time.sleep(3)
                print(driver.find_element(By.TAG_NAME, "h2").text)

    def teardown_class(cls):
        driver.quit()
