import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.login import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
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
