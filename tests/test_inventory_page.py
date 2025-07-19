import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_login_data
from pages.inventory_page import InventoryPage


@pytest.mark.inventory
@pytest.mark.usefixtures('driver')
class TestsInventoryPage:

    def test_inventory_page_loads(self, login_and_go_to_inventory):
        data = load_login_data()[0]
        inventory = login_and_go_to_inventory
        assert inventory.get_current_url() == data['expected_url']

        page_title = inventory.get_inventory_title()

        assert page_title == 'Swag Labs'

    def test_menu_button_visible(self, login_and_go_to_inventory):
        inventory = login_and_go_to_inventory
        nav_menu = inventory.get_inventory_nav_menu()

        assert nav_menu.is_displayed()

    def test_product_list_visible(self, login_and_go_to_inventory):
        inventory = login_and_go_to_inventory
        inventory_count = inventory.get_items_count()

        assert inventory_count > 0

    @pytest.mark.props
    def test_product_has_required_fields(self, login_and_go_to_inventory):
        inventory = login_and_go_to_inventory

        inventory_items = inventory.get_inventory_items_props()

        for index, product in enumerate(inventory_items, start=1):
            assert product['name'], f"Product #{index} is missing a name."
            assert product['description'], f"Product #{index} is missing a description."
            assert product['img'], f"Product #{index} is missing a image."
            assert product['price'], f"Product #{index} is missing a price."
            assert product['button'] == "Add to cart", f"Product #{index} is missing button 'Add to cart'."
