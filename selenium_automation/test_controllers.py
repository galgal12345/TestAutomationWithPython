from threading import Thread
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Test_Controllers:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_controllers.html")

    def test_01basic_operations(self):
        driver.find_element(By.NAME, "firstname").send_keys("Gil")
        driver.find_element(By.NAME, "lastname").send_keys("Almuly")
        my_country = Select(driver.find_element(By.ID, "continents"))
        my_country.select_by_value("europe")
        driver.find_element(By.ID, "submit").click()

    def test_02url_manipulations(self):
        url = driver.current_url
        my_url_parse = urlparse(url)
        my_str_query = my_url_parse[4].split("&")
        assert my_str_query[0] == "firstname=Gil", "Test Failed"
        assert my_str_query[1] == "lastname=Almuly", "Test Failed"
        assert my_str_query[6] == "continents=europe", "Test Failed"
        print("Test Passed")

    def test_03fill_in_all_the_other_fields(self):
        driver.find_element(By.ID, "sex-1").click()
        driver.find_element(By.ID, "exp-4").click()
        driver.find_element(By.ID, "profession-1").click()
        driver.find_element(By.ID, "tool-2").click()
        my_commends = Select(driver.find_element(By.ID, "selenium_commands"))
        my_commends.select_by_value("navigation")
        driver.find_element(By.ID, "datepicker").click()
        data_widget = driver.find_element(By.ID, "ui-datepicker-div")
        cells = data_widget.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            if cell.text == "18":
                cell.click()
                break
        driver.find_element(By.ID, "submit").click()
        url = driver.current_url
        my_url_parse = urlparse(url)
        my_str_query = my_url_parse[4].split("&")
        my_date_picker_str = my_str_query[4].replace("%2F", "-")
        print(my_date_picker_str)

    def teardown_class(cls):
        print("")
        driver.quit()
