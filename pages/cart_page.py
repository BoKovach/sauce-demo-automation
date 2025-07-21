import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_page_url = 'https://www.saucedemo.com/cart.html'
        self.cart_page_title = (By.CSS_SELECTOR, '#header_container > div.primary_header > div.header_label > div')
        self.cart_icon = (By.ID, 'shopping_cart_container')
        self.continue_shopping_button = (By.ID, 'continue-shopping')
        self.product_name = (By.CLASS_NAME, 'inventory_item_name')
        self.product_description = (By.CLASS_NAME, 'inventory_item_desc')
        self.product_price = (By.CLASS_NAME, 'inventory_item_price')
        self.product_quantity = (By.CLASS_NAME, 'cart_quantity')
        self.checkout_button = (By.ID, 'checkout')
        self.remove_product_button = (By.CLASS_NAME, 'btn btn_secondary btn_small cart_button')
        self.product_item = (By.CLASS_NAME, 'cart_item')

    def get_current_url(self):
        return self.driver.current_url

    def get_all_products(self):
        all_products = [el for el in self.driver.find_elements(*self.product_item)]
        return all_products

    def get_product_name(self, product):
        return product.find_element(*self.product_name).text

    def get_product_description(self, product):
        return product.find_element(*self.product_description).text

    def get_product_price(self, product):
        return float(product.find_element(*self.product_price).text.replace('$', ''))

    def get_product_quantity(self, product):
        return product.find_element(*self.product_quantity).text

    def get_product_button(self, product):
        return product.find_element(*self.remove_product_button)

