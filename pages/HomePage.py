from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    header = ".maintext"
    error = ".alert-error"

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.header).text

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error).text
