from selenium import webdriver

class BaseDriver:
    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()  # Ensure chromedriver.exe is in the PATH
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver
