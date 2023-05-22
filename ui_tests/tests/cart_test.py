import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from ui_tests.pages.cart import CartPage
from ui_tests.pages.checkout import CheckoutPage
from ui_tests.pages.login import LoginPage
from ui_tests.pages.products import ProductsPage


class TestCart(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://automationexercise.com/")

        self.products_page = ProductsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

        self.login_page.close_add()
        self.login_page.login_with_email("seleniumremote@gmail.com", "tester")

    def test_search_product(self):
        pass

    def test_add_multiple_products(self):
        self.products_page.add_product_to_cart("unicorn")
        self.products_page.add_product_to_cart("men tshirt")
        self.cart_page.navigate_to_cart()
        self.cart_page.proceed_to_checkout()
        self.checkout_page.get_products_prices()
        self.assertEqual(self.checkout_page.get_total_amount(), sum(self.checkout_page.get_products_prices()))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
