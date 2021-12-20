import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")

    @allure.title("Drag & Drop")
    @allure.description("drag the small box into the big box")
    def test_01drag_and_drop(self):
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")
        action = ActionChains(driver)
        action.drag_and_drop(draggable, droppable).perform()
        assert driver.find_element(By.CSS_SELECTOR, "#droppable > p").is_displayed(), "Test 1 Failed"

    @allure.title("Click & Hold")
    @allure.description("click & hold item 2 and 3")
    def test_02select_second_and_third_in_list_items(self):
        list_items = driver.find_elements(By.CSS_SELECTOR, "#select_items > li")
        action = ActionChains(driver)
        action.click_and_hold(list_items[1]).click_and_hold(list_items[2]).click().perform()

    @allure.title("Double Click")
    @allure.description("double click where it says 'Double-click this paragraph to trigger a function'")
    def test_03double_click(self):
        expected = "Hello World"
        dclick = driver.find_element(By.ID, "dbl_click")
        action = ActionChains(driver)
        action.double_click(dclick).perform()
        assert driver.find_element(By.ID, "demo").text == expected, "Test 3 Failed"

    @allure.title("Mouse Hover")
    @allure.description("moving the mouse where it says 'Move the mouse pointer over this paragraph.'")
    def test_04mouse_hover(self):
        expected = "background-color: rgb(255, 255, 0);"
        action = ActionChains(driver)
        my_elem = driver.find_element(By.ID, "mouse_hover")
        action.move_to_element(my_elem).click().perform()
        actual = driver.find_element(By.ID, "mouse_hover").get_attribute("style")
        assert actual == expected, "Test 4 Failed"

    @allure.title("Scroll Page")
    @allure.description("scrolling the page and then seeing if the element is displayed on the screen")
    def test_05scroll_page(self):
        driver.execute_script("scrollTo(0,1000);")
        assert driver.find_element(By.ID, "scrolled_element").is_displayed()

    def teardown_class(cls):
        time.sleep(1)
        driver.quit()
