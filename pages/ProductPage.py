from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    cart = '.productcart'

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.cart)
