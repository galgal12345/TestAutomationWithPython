import time

import allure
import pytest
import softest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_Todo(softest.TestCase):

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://todomvc.com/examples/react/")
        time.sleep(2)

    @allure.title("Creates New travel List")
    @allure.description("adding new items to the ToDo page")
    def test_01create_new_task(self):
        my_expected_travel_list = ["passport", "visa", "tickets", "laptop", "camera", "sunglasses"]
        for i in range(1, 6):
            driver.find_element(By.CSS_SELECTOR, "input[class='new-todo']").send_keys(my_expected_travel_list[i])
            driver.find_element(By.CSS_SELECTOR, "input[class='new-todo']").send_keys(Keys.ENTER)
            actual = driver.find_element(By.CSS_SELECTOR, " li:nth-child(" + str(i) + ")  label").text
            self.soft_assert(self.assertEqual, actual, my_expected_travel_list[i])

        self.assert_all()

    @allure.title("Deletes All The Items From The List")
    @allure.description("this method deletes all items from the list")
    def test_02delete_task(self):
        list_items = driver.find_elements(By.CSS_SELECTOR, " section > div > section > ul > li")
        for item in list_items:
            action = ActionChains(driver)
            action.move_to_element(item)
            delete = driver.find_element(By.CSS_SELECTOR, " ul > li button[class='destroy']")
            my_bool = action.move_to_element(delete).click().perform()
            self.soft_assert(self.assertFalse, my_bool, "Test Failed")

        self.assert_all()

    @allure.title("Renaming the list with a Shopping List")
    @allure.description("erase the travel list and puts new items for Shopping List")
    def test_03rename_task(self):
        expected_shopping_list = ["Bread", "Cereal", "Eggs", "Milk", "Broccoli"]
        self.test_01create_new_task()
        list_items = driver.find_elements(By.CSS_SELECTOR, " section > div > section > ul > li")
        for i in range(1, len(list_items) + 1):
            action = ActionChains(driver)
            task_box = driver.find_element(By.CSS_SELECTOR, " div > section > ul > li:nth-child(" + str(i) + ")")
            action.move_to_element(task_box)
            action.double_click(task_box).double_click(task_box).send_keys(expected_shopping_list[i - 1]).perform()
            driver.find_element(By.CSS_SELECTOR, "footer > ul").click()
        for i in range(1, len(list_items) + 1):
            actual = driver.find_element(By.CSS_SELECTOR, " li:nth-child(" + str(i) + ")  label").text
            self.soft_assert(self.assertEqual, actual, expected_shopping_list[i - 1], "Test rename_task Failed")

        self.assert_all()

    @allure.title("Mark As Completed")
    @allure.description("marking specific items on the list by checking the toggle with V")
    def test_04mark_as_completed_task(self):
        for i in range(1, 3):
            driver.find_element(By.CSS_SELECTOR, "li:nth-child(" + str(i) + ") > div > input[class=toggle]").click()

    @allure.title("Filter Missions")
    @allure.description("checking if there ara 5 items in page that shows all the items 3 in Active and 2 in Completed")
    def test_05filter_missions(self):

        driver.find_element(By.LINK_TEXT, "Active").click()
        list_items = driver.find_elements(By.CSS_SELECTOR, " section > div > section > ul > li")
        active_size = len(list_items)
        self.soft_assert(self.assertEqual, active_size, 3, "Test Failed")

        driver.find_element(By.LINK_TEXT, "Completed").click()
        list_items = driver.find_elements(By.CSS_SELECTOR, " section > div > section > ul > li")
        completed_size = len(list_items)
        self.soft_assert(self.assertEqual, completed_size, 2, "Test Failed")

        self.soft_assert(self.assertEqual, completed_size + active_size, 5, "Test Failed")

        self.assert_all()

    @allure.title("Delete Completed")
    @allure.description("deletes only the completed tasks")
    def test_06delete_completed(self):
        self.test_02delete_task()

    def teardown_class(cls):
        driver.quit()
