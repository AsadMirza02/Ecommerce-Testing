from framework.base_driver import BaseDriver
from selenium.webdriver.common.by import By

def test_checkout_workflow():
    driver = BaseDriver.get_driver()
    driver.get("https://demo.opencart.com")
    driver.find_element(By.LINK_TEXT, "MacBook").click()
    driver.find_element(By.ID, "button-cart").click()

    driver.find_element(By.LINK_TEXT, "Shopping Cart").click()
    driver.find_element(By.LINK_TEXT, "Checkout").click()

    assert "Checkout" in driver.title
    driver.quit()
