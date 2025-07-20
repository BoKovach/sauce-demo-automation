import pytest
from utils.data_loader import load_login_data, load_sort_menu_data

sort_menu = load_sort_menu_data()


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

    @pytest.mark.sorted
    @pytest.mark.parametrize('data', sort_menu)
    def test_sorted_by_name_and_price(self, login_and_go_to_inventory, data):
        inventory = login_and_go_to_inventory
        inventory.sort_by_text(data['case'])

        sorted_products_name = inventory.get_inventory_items_name()
        sorted_products_price = inventory.get_inventory_items_price()

        if data['type'] == 'ascending_name':
            assert inventory.is_sorted_ascending(sorted_products_name), f"Not sorted A-Z: {sorted_products_name}"

        elif data['type'] == 'descending_name':
            assert inventory.is_sorted_descending(sorted_products_name), f"Not sorted Z-A: {sorted_products_name}"

        elif data['type'] == 'ascending_price':
            assert inventory.is_sorted_ascending(sorted_products_price), f"Not sorted low to high price:" \
                                                                         f" {sorted_products_price}"
        elif data['type'] == 'descending_price':
            assert inventory.is_sorted_descending(sorted_products_price), f"Not sorted high to low price:" \
                                                                         f" {sorted_products_price}"

    @pytest.mark.add
    def test_add_product_to_cart(self, login_and_go_to_inventory):
        inventory = login_and_go_to_inventory
        cart_badge = inventory.get_cart_badge_count()

        assert cart_badge == 0

        product = inventory.get_all_items()[0]
        assert inventory.get_button_text(product) == 'Add to cart'

        inventory.add_product_to_cart(product)
        cart_badge = inventory.get_cart_badge_count()
        assert cart_badge == 1
        assert inventory.get_button_text(product) == 'Remove'

        inventory.remove_product_from_cart(product)

    @pytest.mark.remove
    def test_remove_product_to_cart(self, login_and_go_to_inventory):
        inventory = login_and_go_to_inventory

        product = inventory.get_all_items()[0]
        inventory.add_product_to_cart(product)
        cart_badge = inventory.get_cart_badge_count()

        assert cart_badge == 1
        assert inventory.get_button_text(product) == 'Remove'

        inventory.remove_product_from_cart(product)
        cart_badge = inventory.get_cart_badge_count()
        assert cart_badge == 0
        assert inventory.get_button_text(product) == 'Add to cart'
