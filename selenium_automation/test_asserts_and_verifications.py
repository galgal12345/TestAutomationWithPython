from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_LocatorsBasic:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/bmi/")

    def test_01bmi(self):
        expected_result = ["21", "That you are healthy."]
        driver.find_element(By.ID, "weight").send_keys("63")
        driver.find_element(By.ID, "hight").send_keys("172")
        driver.find_element(By.ID, "calculate_data").click()
        assert driver.find_element(By.ID, "bmi_result").get_attribute("value") == expected_result[0], "Test Failed"
        assert driver.find_element(By.ID, "bmi_means").get_attribute("value") == expected_result[1], "Test Failed"

    def teardown_class(cls):
        driver.quit()
