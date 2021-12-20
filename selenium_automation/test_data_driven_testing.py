import time

import allure
import pytest
import softest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_DataDrivenTesting:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.wikipedia.org/")

    @pytest.mark.parametrize("text_search, expected_title",
                             [("Israel", "Israel"),
                              ("Automation", "Automation"),
                              ("BlahBlah", "Search results")])
    def test_01send_to_wiki(self, text_search, expected_title):
        driver.find_element(By.ID, "searchInput").send_keys(text_search)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        actual_title = driver.find_element(By.ID, "firstHeading").text
        assert actual_title == expected_title, "Test Failed"
        driver.get("https://www.wikipedia.org/")

    def teardown_class(cls):
        driver.quit()
