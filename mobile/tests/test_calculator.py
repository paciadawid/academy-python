import os
import unittest

from appium import webdriver

from mobile.screens.main import MainScreen


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

        self.main_screen = MainScreen(self.driver)

    def test_add_2_values(self):
        self.main_screen.add_values(5, 7)
        self.assertEqual(12, self.main_screen.get_result())

    def test_arcsin_out_of_range(self):
        self.main_screen.arcsin(9)
        self.assertEqual("Domain error", self.main_screen.get_message_error())

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
