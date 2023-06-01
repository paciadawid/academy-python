import unittest
import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:

        # Returns abs path relative to this file and not cwd
        app_name = "calculator.apk"
        app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = app_path
        desired_caps["automationName"] = "uiautomator2"

        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)

    def test_add_2_values(self):
        self.driver.find_element(AppiumBy.ID, "digit_1").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plus").click()
        self.driver.find_element(AppiumBy.ID, "digit_2").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
        result = self.driver.find_element(AppiumBy.ID, "result_final").text
        self.assertEqual(3, int(result))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
