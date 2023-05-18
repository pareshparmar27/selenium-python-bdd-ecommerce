from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    header = ".maintext"
    error = ".alert-error"
    categories = '.categorymenu > li > a'
    subCategories = '.subcategories > ul > li'
    productList = '.list-inline > div:not(.clearfix)'
    currency = '.language'
    currencyList = '.currency > li'
    price = '.price > div'

    def __init__(self, driver):
        super().__init__(driver)

    def get_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.header).text

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error).text

    def search(self, category, subcategory):
        action = ActionChains(self.driver)
        all_categories = self.driver.find_elements(By.CSS_SELECTOR, self.categories)
        for each_cat in all_categories:
            if category in each_cat.text:
                action.move_to_element(each_cat).perform()
                break
        all_sub_categories = self.driver.find_elements(By.CSS_SELECTOR, self.subCategories)
        for each_sub_cat in all_sub_categories:
            if subcategory in each_sub_cat.text:
                each_sub_cat.click()
                break

    def get_product_count(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, self.productList))

    def select_currency(self, currency):
        action = ActionChains(self.driver)
        currency_ele = self.driver.find_element(By.CSS_SELECTOR, self.currency)
        action.move_to_element(currency_ele).perform()
        currency_list = self.driver.find_elements(By.CSS_SELECTOR, self.currencyList)
        for each in currency_list:
            if currency.upper() in each.text:
                each.click()
                break

    def check_products_currency(self, currency):
        expected_currency_code = self.get_currency_code(currency)
        product_list = self.driver.find_elements(By.CSS_SELECTOR, self.productList)
        for each in product_list:
            actual_currency_code = each.find_element(By.CSS_SELECTOR, self.price).text
            assert expected_currency_code in actual_currency_code

    @staticmethod
    def get_currency_code(currency):
        match currency.upper():
            case "EURO":
                return "€"
            case "US DOLLAR":
                return "$"
            case "POUND STERLING":
                return "£"
            case default:
                raise ValueError(currency + " currency is not supported...")
