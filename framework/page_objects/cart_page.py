from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".table-responsive .text-left")

    def remove_item(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
