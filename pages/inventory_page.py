from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, 'inventory_item')
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add_to_cart')]")
        self.remove_button = (By.XPATH, "//button[contains(text(), 'Remove')]")
        self.shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')

    def get_items_count(self):
        return len(self.driver.find_elements(*self.inventory_item))

    def add_product_to_cart(self):
        add_button = self.driver.find_element(*self.add_to_cart_button)
        add_button.click()

    def remove_product(self):
        remove_button = self.driver.find_element(*self.remove_button)
        remove_button.click()

    def get_cart_badge_account(self):
        badge = self.driver.find_element(*self.shopping_cart_badge)
        return int(badge.text)

    def go_to_cart(self):
        cart_link = self.driver.find_element(*self.shopping_cart_link)
        cart_link.click()
        