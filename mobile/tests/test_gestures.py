import os
import time
import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from mobile.helpers.gestures import find_element_with_scrolls


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        app_name = "gestures.apk"
        app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), app_name))

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['app'] = app_path
        desired_caps["automationName"] = "uiautomator2"
        desired_caps["newCommandTimeout"] = 300

        desired_caps["appPackage"] = "com.wdiodemoapp"
        desired_caps["appActivity"] = "com.wdiodemoapp.MainActivity"

        self.driver = webdriver.Remote('http://localhost:4723', desired_caps)
        self.driver.implicitly_wait(10)

    def test_swipe_vertical(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        self.assertTrue(find_element_with_scrolls(self.driver, (AppiumBy.ACCESSIBILITY_ID, "WebdriverIO logo"), "UP"))

    def test_swipe_horizontal(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        self.assertTrue(
            find_element_with_scrolls(self.driver, (AppiumBy.XPATH, "//*[contains(@text, 'COMPATIBLE')]"), "LEFT"))

    def test_drag_and_drop(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag").click()
        drag_elements = self.driver.find_elements(AppiumBy.XPATH, "//*[contains(@content-desc, 'drag')]")
        for drag_element in drag_elements:
            tile_position = drag_element.get_attribute("content-desc").split("-")[-1]
            drop_element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"drop-{tile_position}")
            self.driver.drag_and_drop(drag_element, drop_element)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "button-Retry")))

    def test_webview(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Webview").click()
        time.sleep(5)
        self.driver.switch_to.context(self.driver.contexts[1])
        time.sleep(5)
        self.driver.find_element(By.ID, "__docusaurus")


if __name__ == '__main__':
    unittest.main()
