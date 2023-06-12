import os
import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from mobile.helpers.gestures import find_element_with_scrolls

number_of_scrolls = 5

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        app_name = "gestures.apk"
        app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = app_path
        desired_caps["automationName"] = "uiautomator2"

        desired_caps["appPackage"] = "com.wdiodemoapp"
        desired_caps["appActivity"] = "com.wdiodemoapp.MainActivity"

        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)
        self.driver.implicitly_wait(5)

    def test_swipe_vertical(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        self.assertTrue(find_element_with_scrolls(self.driver, (AppiumBy.ACCESSIBILITY_ID, "WebdriverIO logo"), "UP"))

    def test_swipe_horizontal(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        self.assertTrue(find_element_with_scrolls(self.driver, (AppiumBy.XPATH, "//*[contains(@text, 'COMPATIBLE')]"), "LEFT"))




if __name__ == '__main__':
    unittest.main()
