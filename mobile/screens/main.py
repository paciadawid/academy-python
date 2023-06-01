from appium.webdriver.common.appiumby import AppiumBy

from mobile.screens.base import BaseScreen


class MainScreen(BaseScreen):
    final_result_selector = (AppiumBy.ID, "result_final")
    plus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "plus")
    equals_button_selector = (AppiumBy.ACCESSIBILITY_ID, "equals")
    expand_arrow_selector = (AppiumBy.ACCESSIBILITY_ID, "Expand")
    inverse_button_selector = (AppiumBy.ACCESSIBILITY_ID, "show inverse functions")
    arcsinus_button_selector = (AppiumBy.ACCESSIBILITY_ID, "inverse sine")
    parenthesis_button_selector = (AppiumBy.ACCESSIBILITY_ID, "left or right parenthesis")
    result_preview_selector = (AppiumBy.ID, "result_preview")

    # dynamic selectors
    digit_button_selector = (AppiumBy.ID, "digit_{digit}")

    def add_values(self, value1, value2):
        self.driver.find_element(*self.parse_digit_selector(value1)).click()
        self.driver.find_element(*self.plus_button_selector).click()
        self.driver.find_element(*self.parse_digit_selector(value2)).click()
        self.driver.find_element(*self.equals_button_selector).click()

    def arcsin(self, radians):
        self.driver.find_element(*self.expand_arrow_selector).click()
        self.driver.find_element(*self.inverse_button_selector).click()
        self.driver.find_element(*self.arcsinus_button_selector).click()
        self.driver.find_element(*self.parse_digit_selector(radians)).click()
        self.driver.find_element(*self.parenthesis_button_selector).click()
        self.driver.find_element(*self.equals_button_selector).click()

    def get_message_error(self):
        message = self.driver.find_element(*self.result_preview_selector).text
        return message
    def get_result(self):
        result = self.driver.find_element(*self.final_result_selector).text
        return int(result)

    def parse_digit_selector(self, digit):
        selector = (self.digit_button_selector[0], self.digit_button_selector[1].format(digit=digit))
        return selector
