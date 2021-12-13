from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_NopCommerce:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.nopcommerce.com/")

    def test_01filter_price_low_to_high(self):
        print("test_01filter_price_low_to_high")

    def test_02verify_three_products_in_total(self):
        print("test_02verify_three_products_in_total")

    def test_03verify_product_names_match_to_expected(self):
        print("test_03verify_product_names_match_to_expected")

    def test_03verify_three_stars_or_higher(self):
        print("test_03verify_three_stars_or_higher")

    def teardown_class(cls):
        driver.quit()
