import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_Pizza:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://atidcollege.co.il/Xamples/pizza/")

    def test_01(self):
        expected_list = "$7.50"
        actual = driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']").text
        assert actual == expected_list, "Test 1 Failed"

    def test_02(self):
        driver.find_element(By.CSS_SELECTOR, "#input_5_22_3").send_keys("Gil")
        driver.find_element(By.CSS_SELECTOR, "#input_5_22_6").send_keys("Almuly")
        delivery_type = Select(driver.find_element(By.ID, "input_5_21"))
        delivery_type.select_by_value("Delivery|3")
        expected_list = "$10.50"
        actual = driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']").text
        assert actual == expected_list, "Test 2 Failed"

    def test_03(self):
        expected = "Gil Almuly 088-234"
        win_handle = driver.current_window_handle
        ifrm = driver.find_element(By.CSS_SELECTOR, "#field_5_19 > iframe")
        driver.switch_to.frame(ifrm)
        coupon = driver.find_element(By.CSS_SELECTOR, "#coupon_Number").text
        driver.switch_to.default_content()
        driver.find_element(By.CSS_SELECTOR, "#input_5_20").send_keys(coupon)
        driver.find_element(By.CSS_SELECTOR, "#gform_submit_button_5").click()
        popup = driver.switch_to.alert
        alert_txt = popup.text
        popup.accept()
        driver.switch_to.window(win_handle)
        driver.close()
        assert alert_txt == expected, "Test 3 Failed"

    def teardown_class(cls):
        driver.quit()
