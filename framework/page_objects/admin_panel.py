from selenium.webdriver.common.by import By

class AdminPanel:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "input-username").send_keys(username)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
