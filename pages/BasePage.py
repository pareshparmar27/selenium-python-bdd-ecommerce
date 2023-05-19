from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import ConfigReader


class BasePage:
    header = ".maintext"
    continue_button = '[title="Continue"]'
    confirm_button = '#checkout_btn'
    checkout = '[data-id="menu_checkout"]'

    def __init__(self, driver):
        self.driver = driver

    def get_header(self):
        WebDriverWait(self.driver, ConfigReader.read_file("timeouts", "explicit_wait")).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.header)))
        return self.driver.find_element(By.CSS_SELECTOR, self.header)

    def click_button(self, button_name):
        match button_name.upper():
            case "CONTINUE":
                self.driver.find_element(By.CSS_SELECTOR, self.continue_button).click()
            case "CONFIRM ORDER":
                self.driver.find_element(By.CSS_SELECTOR, self.confirm_button).click()
            case "CHECKOUT":
                self.driver.find_elements(By.CSS_SELECTOR, self.checkout)[0].click()
            case default:
                raise ValueError(button_name + " button not found")

    def wait_until_text_visibility(self, element, text):
        WebDriverWait(self.driver, ConfigReader.read_file("timeouts", "explicit_wait")).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, element), text))
