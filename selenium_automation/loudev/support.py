from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Support:

    def verify_elements(self, driver):
        elements = driver.find_elements(By.CSS_SELECTOR, "#ms-aloha li[class='ms-elem-selectable']")
        my_size_list_elem = len(elements)
        assert elements[0].text == "elem 3", "Test Failed"
        assert elements[my_size_list_elem - 1].text == "elem 20", "Test Failed"
