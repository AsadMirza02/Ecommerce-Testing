from framework.base_driver import BaseDriver
from framework.page_objects.homepage import HomePage

def test_product_search():
    driver = BaseDriver.get_driver()
    driver.get("https://demo.opencart.com")
    homepage = HomePage(driver)
    homepage.search_product("MacBook")
    assert "MacBook" in driver.page_source
    driver.quit()
