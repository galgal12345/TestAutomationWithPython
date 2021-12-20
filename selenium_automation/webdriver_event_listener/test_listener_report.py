from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_automation.webdriver_event_listener.event_listener import EventListener


class TestListenerReport:
    def setup_class(cls):
        global driver
        edriver = webdriver.Chrome(ChromeDriverManager().install())
        driver = EventFiringWebDriver(edriver, EventListener())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(2)

    def test_1(self):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']").click()
        assert driver.find_element(By.CLASS_NAME, "title").text == "PRODUCTS"
        driver.back()
        driver.forward()

    def teardown_class(cls):
        driver.quit()
