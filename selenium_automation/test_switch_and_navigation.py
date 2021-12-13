from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_SwitchAndNavigation:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://atidcollege.co.il/Xamples/ex_switch_navigation.html")

    def test_01switch_to_alert(self):
        driver.find_element(By.ID, "btnAlert").click()
        popup = driver.switch_to.alert
        print(popup.text)
        popup.accept()
        assert driver.find_element(By.ID, "output").text == "Alert is gone.", "Test Failed"

    def test_02prompt(self):
        driver.find_element(By.ID, "btnPrompt").click()
        popup = driver.switch_to.alert
        print(popup.text)
        popup.send_keys("Gil Almuly")
        popup.accept()
        assert driver.find_element(By.ID, "output").text == "Gil Almuly", "Test Failed"

    def test_03print_and_verify_iframe_txt(self):
        ifrm = driver.find_element(By.CSS_SELECTOR, "#contact_info_left iframe")
        driver.switch_to.frame(ifrm)
        print(driver.find_element(By.ID, "iframe_container").text)
        actual = driver.find_element(By.ID, "iframe_container").text
        driver.switch_to.default_content()
        assert actual == "This is an IFrame !", "Test Failed"

    def test_04win_handle(self):
        driver.find_element(By.ID, "btnNewTab").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        print(driver.find_element(By.ID, "new_tab_container").text)
        actual = driver.find_element(By.ID, "new_tab_container").text
        assert actual == "This is a new tab", "Test Failed"
        driver.close()
        driver.switch_to.window(handles[0])

    def test_05(self):
        driver.find_element(By.CSS_SELECTOR, "#contact_info_left > a").click()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        print(driver.find_element(By.ID, "new_window_container").text)
        actual = driver.find_element(By.ID, "new_window_container").text
        assert actual == "This is a new window", "Test Failed"
        driver.close()
        driver.switch_to.window(handles[0])

    def teardown_class(cls):
        driver.quit()
