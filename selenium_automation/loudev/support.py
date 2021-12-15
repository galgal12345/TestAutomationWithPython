from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Support:

    def verify_elements(self, driver):

        expected = 'my_elem '
        elements = driver.find_elements(By.CSS_SELECTOR, "#ms-aloha li[class='ms-my_elem-selectable']")
        for i in range(len(elements)):
            if "selected" not in elements[i].get_attribute("class"):
                actual = elements[i].find_element(By.TAG_NAME, "span").text
                assert actual == expected + str(i), "Test Failed"
