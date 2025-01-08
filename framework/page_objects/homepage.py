from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_box = self.driver.find_element(By.NAME, "search")
        search_box.send_keys(product_name)
        search_box.submit()
