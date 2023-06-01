from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BaseScreen


class MainScreen(BaseScreen):
    final_result_selector = (AppiumBy.ID, "result_final")
    plus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "plus")
    equals_button_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")

    # dynamic selectors
    digit_button_selector = (AppiumBy.ID, "digit_{digit}")

    def add_values(self, value1, value2):
        self.driver.find_element(*self.parse_digit_selector(value1)).click()
        self.driver.find_element(*self.plus_button_selector).click()
        self.driver.find_element(*self.parse_digit_selector(value2)).click()
        self.driver.find_element(*self.equals_button_selector).click()

    def get_result(self):
        result = self.driver.find_element(AppiumBy.ID, "result_final").text
        return int(result)

    def parse_digit_selector(self, digit):
        selector = (self.digit_button_selector[0], self.digit_button_selector[1].format(digit=digit))
        return selector
