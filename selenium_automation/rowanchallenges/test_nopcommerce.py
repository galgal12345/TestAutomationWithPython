from async_generator._tests.test_async_generator import double
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_NopCommerce:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.nopcommerce.com/")

    def test_01filter_price_low_to_high(self):
        new_list = []
        driver.find_element(By.CSS_SELECTOR, "ul.top-menu.notmobile > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, " a > img[alt='Picture for category Camera & photo']").click()
        my_list = driver.find_elements(By.CSS_SELECTOR, "div.prices > span")
        for any_item in my_list:
            new_list += any_item.text.split()
        new_list.pop(0)
        new_list[0], new_list[1] = new_list[1], new_list[0]
        print(new_list)

    def test_02verify_three_products_in_total(self):
        my_list = driver.find_elements(By.CSS_SELECTOR, "div.prices > span")
        assert len(my_list) == 3

    def test_03verify_product_names_match_to_expected(self):
        expected_list = ["Nikon D5500 DSLR", "Leica T Mirrorless Digital Camera", "Apple iCam"]
        my_list = driver.find_elements(By.CSS_SELECTOR, "h2 > a")
        for i in range(len(my_list)):
            assert my_list[i].text == expected_list[i]

    def test_03verify_three_stars_or_higher(self):
        my_star_list = driver.find_elements(By.CSS_SELECTOR, " div[style*='width']")
        for i in range(len(my_star_list)):
            assert len(my_star_list[i].get_attribute("style")) > 10, "Test Failed"

    def teardown_class(cls):
        driver.quit()
