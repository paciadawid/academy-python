from selenium.webdriver.common.by import By

from ui_tests.pages.base import BasePage


class CartPage(BasePage):
    cart_tab_selector = (By.CLASS_NAME, "fa-shopping-cart")
    checkout_tab_selector = (By.CLASS_NAME, "check_out")

    def navigate_to_cart(self):
        self.driver.find_element(*self.cart_tab_selector).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_tab_selector).click()
