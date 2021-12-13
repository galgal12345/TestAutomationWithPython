from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_LocatorsAdvanced:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_locators.html")

    def test_01locators_advanced(self):
        print(driver.find_element(By.ID, "locator_id").text)
        print(driver.find_element(By.NAME, "locator_name").text)
        print(driver.find_element(By.TAG_NAME, "p").text)
        print(driver.find_element(By.CLASS_NAME, "locator_class").text)
        print(driver.find_element(By.LINK_TEXT, "myLocator(5)").text)
        print(driver.find_element(By.PARTIAL_LINK_TEXT, "Find").text)
        print(driver.find_element(By.CSS_SELECTOR, "input[myname='selenium']").get_attribute("value"))
        print(driver.find_element(By.XPATH, "//button").text)

    def teardown_class(cls):
        driver.quit()
