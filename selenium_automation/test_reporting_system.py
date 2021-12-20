import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_ReportingSystem:
    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://admin-demo.nopcommerce.com")

    @allure.title("Login Page")
    @allure.description("sending email and password and then verifying  title")
    def test_verify_login(self):
        try:
            self.step_login("admin@yourstore.com", "admin")
            self.step_verify_title()

        except Exception as e:

            self.attach_file()
            print("Test failed, see details: ", e)
            pytest.fail("Test failed, see details: ", e)

    @allure.step("clearing sending and clicking on login page")
    def step_login(self, email, password):
        # clearing the text boxes in the page
        driver.find_element(By.ID, "Email").clear()
        driver.find_element(By.ID, "Password").clear()
        # sending keys to the email and password text boxes
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        # clicking on the submit button
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    @allure.step("check if the title is displayed on screen")
    def step_verify_title(self):
        assert driver.find_element(By.CSS_SELECTOR, "div[class='content-header'] > h1").is_displayed(), "Test Failed"

    def attach_file(self):
        image = "C:/Users/GIL/PycharmProjects/TestAutomationWithPython/screen-shots/screen.png"
        driver.get_screenshot_as_file(image)
        allure.attach.file(image, attachment_type=allure.attachment_type.PNG)

    def teardown_class(cls):
        driver.quit()
