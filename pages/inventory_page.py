from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_title = (By.CSS_SELECTOR, '#header_container > div.primary_header > div.header_label > div')
        self.inventory_nav_menu = (By.ID, 'react-burger-menu-btn')
        self.product_dropdown_menu = (By.CLASS_NAME, 'product_sort_container')
        self.inventory_item = (By.CLASS_NAME, 'inventory_item')
        self.inventory_item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.inventory_item_price = (By.CLASS_NAME, 'inventory_item_price')
        self.inventory_item_description = (By.CLASS_NAME, 'inventory_item_desc')
        self.inventory_item_img = (By.CLASS_NAME, 'inventory_item_img')
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.remove_button = (By.XPATH, "//button[contains(text(), 'Remove')]")
        self.shopping_cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')

    def get_current_url(self):
        return self.driver.current_url

    def get_inventory_title(self):
        return self.driver.find_element(*self.inventory_title).text

    def get_inventory_nav_menu(self):
        return self.driver.find_element(*self.inventory_nav_menu)

    def sort_by_text(self, text):
        dropdown = Select(self.driver.find_element(*self.product_dropdown_menu))
        dropdown.select_by_visible_text(text)

    def is_sorted_ascending(self, values):
        return values == sorted(values)

    def is_sorted_descending(self, values):
        return values == sorted(values, reverse=True)

    def get_all_items(self):
        return self.driver.find_elements(*self.inventory_item)

    def get_items_count(self):
        return len(self.driver.find_elements(*self.inventory_item))

    def get_button_text(self, item):
        return item.find_element(By.TAG_NAME, 'button').text

    def get_inventory_items_props(self):
        items = [el for el in self.driver.find_elements(*self.inventory_item)]
        all_items = []

        for current_item in items:
            try:
                current_item.find_element(*self.inventory_item_img)
                img = True
            except NoSuchElementException:
                img = False

            item_obj = {
                'name': current_item.find_element(*self.inventory_item_name).text,
                'description': current_item.find_element(*self.inventory_item_description).text,
                'img': img,
                'price': current_item.find_element(*self.inventory_item_price).text,
                'button': current_item.find_element(*self.add_to_cart_button).text,
            }

            all_items.append(item_obj)

        return all_items

    def get_inventory_items_name(self):
        names = [el.text for el in self.driver.find_elements(*self.inventory_item_name)]
        return names

    def get_inventory_items_price(self):
        prices = [float(el.text.replace('$', '')) for el in self.driver.find_elements(*self.inventory_item_price)]
        return prices

    def add_product_to_cart(self, item):
        add_button = item.find_element(*self.add_to_cart_button)
        add_button.click()

    def remove_product_from_cart(self, item):
        remove_button = item.find_element(*self.remove_button)
        remove_button.click()

    def get_cart_badge_count(self):
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.shopping_cart_badge)
            )
            return int(badge.text)
        except:
            return 0

    def go_to_cart(self):
        cart_link = self.driver.find_element(*self.shopping_cart_link)
        cart_link.click()
