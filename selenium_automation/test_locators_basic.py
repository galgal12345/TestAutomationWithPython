from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_LocatorsBasic:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())


    def test_01selenium(self):
        driver.get("https://www.selenium.dev/")
        print(driver.find_element(By.ID, "selenium_logo").text)
        print(driver.find_element(By.CLASS_NAME, "navbar-logo").text)
        print(driver.find_element(By.CLASS_NAME, "navbar-brand").text)
        print(driver.find_element(By.TAG_NAME, "svg").text)
        print("total links in page: ", len(driver.find_elements(By.TAG_NAME, "a")))
        print("Selenium is: ", len(driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")))
        print("selenium is: ", len(driver.find_elements(By.PARTIAL_LINK_TEXT, "selenium")))

    def test_02wikipedia(self):
        driver.get("https://www.wikipedia.org/")
        logo: WebElement = driver.find_element(By.CLASS_NAME, "central-featured-logo")
        search_input: WebElement = driver.find_element(By.ID, "searchInput")
        search_language: WebElement = driver.find_element(By.ID, "searchLanguage")
        footer: WebElement = driver.find_element(By.CLASS_NAME, "footer-sidebar-content")
        my_elements = [logo, search_input, search_language, footer]

        for element in reversed(my_elements):
            print(element.text)

    def teardown_class(cls):
        driver.quit()
