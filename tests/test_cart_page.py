import pytest


class TestCartPage:

    @pytest.mark.cart
    def test_user_redirected_to_cart_page(self, add_product_and_go_to_cart):
        cart = add_product_and_go_to_cart
        assert cart.get_current_url() == cart.cart_page_url

    @pytest.mark.count
    def test_is_not_empty_cart(self, add_product_and_go_to_cart):
        cart = add_product_and_go_to_cart
        assert cart.get_cart_items_count() > 0

    @pytest.mark.correct_added
    def test_correct_product_is_added_to_cart(self, add_product_and_go_to_cart):
        cart, expected_item_name = add_product_and_go_to_cart

        cart_item = cart.get_cart_items()[0]
        actual_item_name = cart.get_item_name(cart_item)

        assert expected_item_name == actual_item_name

    @pytest.mark.attributes
    def test_product_has_name_description_price_and_quantity(self, add_product_and_go_to_cart):
        cart = add_product_and_go_to_cart
        product = cart.get_cart_items()[0]

        assert cart.get_item_name(product) != ""
        assert cart.get_item_description(product) != ""
        assert cart.get_item_price(product)
        assert cart.get_item_quantity(product) > 0

