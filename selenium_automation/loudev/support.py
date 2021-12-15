import softest
from selenium.webdriver.common.by import By


class Support(softest.TestCase):

    def verify_elements(self, driver):
        elements = driver.find_elements(By.CSS_SELECTOR, "#ms-aloha li[class='ms-elem-selectable']")
        number: int = int(elements[0].find_element(By.TAG_NAME, "span").text[5::])
        for i in range(len(elements)):
            actual = elements[i].find_element(By.TAG_NAME, "span").text
            expected = 'elem ' + str(number)
            self.soft_assert(self.assertTrue, actual == expected, "Test Failed")
            number += 1

        self.assert_all()
