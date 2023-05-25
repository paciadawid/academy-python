import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from broser_config import chrome_config
from ui_tests.pages.login import LoginPage

browser = "chrome"


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "edge":
            options = EdgeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        else:
            raise ValueError(f"No browser called {browser}")

        for argument in chrome_config:
            options.add_argument(argument)

        self.driver = webdriver.Remote("http://192.168.1.28:4444", options=options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")
        self.login_page = LoginPage(self.driver)

    def test_success_login(self):
        self.login_page.login_with_email("seleniumremote@gmail.com", "tester")
        self.login_page.check_if_logged_in()

    def test_empty_password(self):
        self.login_page.login_with_email("seleniumremote@gmail.com", "")
        self.assertTrue(self.login_page.check_password_field_validation())

    def test_wrong_password(self):
        self.login_page.login_with_email("seleniumremote@gmail.com", "nietester")
        self.login_page.check_error_message()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
