import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")

    def test_success_login(self):
        self.driver.find_element(By.XPATH, "//a[@href='/login']").click()
        self.driver.find_element(By.NAME, "email").send_keys("seleniumremote@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("tester")
        self.driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

        # self.driver.find_element(By.CSS_SELECTOR, ".fa-user")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-user")))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
