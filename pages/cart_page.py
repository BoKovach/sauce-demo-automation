from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def wait_for_cart_page(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains("/cart.html"))

    def get_cart_items(self):
        return self.driver.find_elements(*self.product_item)

    def get_cart_items_count(self):
        return len(self.get_cart_items())

    def get_item_name(self, item):
        return item.find_element(*self.product_name).text

    def get_item_description(self, item):
        return item.find_element(*self.product_description).text

    def get_item_price(self, item):
        return float(item.find_element(*self.product_price).text.replace('$', ''))

    def get_item_quantity(self, item):
        return int(item.find_element(*self.product_quantity).text)

    def get_remove_item_button(self, item):
        return item.find_element(*self.remove_product_button)

    def remove_item(self, item):
        self.get_remove_item_button(item).click()

    def click_continue_shopping_button(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def is_cart_empty(self):
        return self.get_cart_items_count() == 0

