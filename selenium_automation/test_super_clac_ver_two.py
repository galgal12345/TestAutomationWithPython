import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Test_SuperClacVerTwo:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_01(self):
        global my_list
        driver.get("https://www.random.org/")
        ifrm = driver.find_element(By.CSS_SELECTOR, "#homepage-generator > iframe")
        driver.switch_to.frame(ifrm)
        driver.find_element(By.CSS_SELECTOR, "input[id*=max]").clear()
        driver.find_element(By.CSS_SELECTOR, "input[id*=max]").send_keys("10")
        driver.find_element(By.CSS_SELECTOR, "input[id*=button]").click()
        time.sleep(1)
        my_rnd_num = driver.find_element(By.CSS_SELECTOR, "span[id*='result'] span:nth-child(1)").text
        driver.switch_to.default_content()

        driver.get("http://juliemr.github.io/protractor-demo/")

        operator = Select(driver.find_element(By.CSS_SELECTOR, " form select"))
        operator.select_by_visible_text("*")

        for i in range(0, int(my_rnd_num) + 1):
            right_field = my_rnd_num
            left_field = str(i)
            driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").send_keys(right_field)
            driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys(left_field)
            driver.find_element(By.ID, "gobutton").click()
            time.sleep(3)

        counter = 0
        for x in range(1, int(my_rnd_num) + 1):
            counter += int(driver.find_element(By.CSS_SELECTOR, "tr:nth-child(" + str(x) + ") > td:nth-child(3)").text)

        print("The Random Number Is: ", my_rnd_num)
        print("The Result Of Number ", my_rnd_num, " is ", counter)

    def teardown_class(cls):
        driver.quit()
