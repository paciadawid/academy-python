from selenium.webdriver.common.by import By

from ui_tests.pages.base import BasePage


class CheckoutPage(BasePage):

    price_element_selector = (By.CLASS_NAME, "cart_total_price")

    def get_products_prices(self):
        prices_elements = self.driver.find_elements(*self.price_element_selector)[:-1]
        prices = []
        for element in prices_elements:
            prices.append(int(element.text[4:]))
        return prices

    def get_total_amount(self):
        total_amount_element = self.driver.find_elements(*self.price_element_selector)[-1]
        return int(total_amount_element.text[4:])
