import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")

    def test_search_product(self):
        self.driver.find_element(By.XPATH, "//*[@href='/products']").click()
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//*[@href='/products']").click()
        self.driver.find_element(By.ID, "search_product").send_keys("unicorn")
        self.driver.find_element(By.ID, "submit_search").click()

        # 1
        self.driver.find_element(By.CLASS_NAME, "single-products")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "single-products")))

        # 2
        products_list = self.driver.find_elements(By.CLASS_NAME, "single-products")
        self.assertGreaterEqual(len(products_list), 2)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
