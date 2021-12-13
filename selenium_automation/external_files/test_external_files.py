from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:/Users/GIL/PycharmProjects/TestAutomationWithPython/Config file/config.xml').getroot()
    return root.find(".//" + node_name).text


class Test_ExternalFiles:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(get_data("Url"))

    def test_01(self):
        driver.find_element(By.ID, "weight").send_keys(get_data("Weight"))
        driver.find_element(By.ID, "hight").send_keys(get_data("Height"))
        driver.find_element(By.ID, "calculate_data").click()

        expected_result = get_data("ExpectedResultBMI")
        actual_result = driver.find_element(By.ID, "bmi_result").get_attribute("value")
        assert expected_result == actual_result

    def teardown_class(cls):
        driver.quit()
