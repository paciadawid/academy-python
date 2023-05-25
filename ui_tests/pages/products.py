from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui_tests.pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.XPATH, "//*[@href='/products']")
    search_field_selector = (By.ID, "search_product")
    product_tile_selector = (By.CLASS_NAME, "single-products")
    submit_search_button_selector = (By.ID, "submit_search")
    add_to_cart_button_selector = (By.CSS_SELECTOR, ".overlay-content > .add-to-cart")
    continue_shopping_button_selector = (By.CLASS_NAME, "btn-success")

    def search_product(self, product_name):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.find_element(*self.search_field_selector).send_keys(product_name)
        self.driver.find_element(*self.search_field_selector).click()

    def add_product_to_cart(self, product_name):
        self.search_product(product_name)

        overlay_element = self.driver.find_element(*self.product_tile_selector)
        ActionChains(self.driver).move_to_element(overlay_element).perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_to_cart_button_selector)).click()

        self.driver.find_element(*self.continue_shopping_button_selector).click()
