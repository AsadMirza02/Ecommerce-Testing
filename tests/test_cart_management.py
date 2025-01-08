from framework.base_driver import BaseDriver
from framework.page_objects.homepage import HomePage
from framework.page_objects.cart_page import CartPage

def test_cart_management():
    driver = BaseDriver.get_driver()
    driver.get("https://demo.opencart.com")
    homepage = HomePage(driver)
    homepage.search_product("MacBook")
    driver.find_element_by_link_text("MacBook").click()
    driver.find_element_by_id("button-cart").click()

    cart = CartPage(driver)
    cart_items = cart.get_cart_items()
    assert any("MacBook" in item.text for item in cart_items)

    cart.remove_item()
    assert not cart.get_cart_items()
    driver.quit()
