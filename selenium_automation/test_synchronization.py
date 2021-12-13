from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Test_Synchronization:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://atidcollege.co.il/Xamples/ex_synchronization.html")

    def test_01(self):
        driver.find_element(By.ID, "rendered").click()
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element((By.ID, "finish2"), "My Rendered Element After Fact!"))
        actual = driver.find_element(By.ID, "finish2").text
        assert actual == "My Rendered Element After Fact!"

    def test_02(self):
        driver.find_element(By.ID, "hidden").click()
        time.sleep(1)
        actual = driver.find_element(By.ID, "loading1").is_displayed()
        assert actual, "Test Failed"

    def test_03(self):
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "btn").click()
        actual = driver.find_element(By.ID, "message").text
        assert actual == "It's gone!", "Test Failed"


    def teardown_class(cls):
        driver.quit()
