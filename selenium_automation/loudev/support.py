from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Support:

    def verify_elements(self, driver):
        i = 2
        expected = 'elem '
        elements = driver.find_elements(By.CSS_SELECTOR, "#ms-aloha li[class='ms-elem-selectable']")
        for elem in elements:
            i += 1
            if "ms-selected" not in elem.get_attribute("class"):
                actual = elem.find_element(By.TAG_NAME, "span").text
                assert actual == expected + str(i), "Test Failed"
