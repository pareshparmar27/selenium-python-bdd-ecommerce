from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from utils import ConfigReader


class LoginPage(BasePage):
    username = "#loginFrm_loginname"
    password = "#loginFrm_password"
    signin = "[title=\"Login\"]"
    account_register = "#accountFrm_accountregister"
    account_guest = "#accountFrm_accountguest"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.username).send_keys("username")
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys("password")
        self.driver.find_element(By.CSS_SELECTOR, self.signin).click()

    def login_with_params(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.username).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.signin).click()

    def select_account(self, account_type):
        match account_type.upper():
            case "REGISTER":
                self.driver.find_element(By.CSS_SELECTOR, self.account_register).click()
            case "GUEST":
                self.driver.find_element(By.CSS_SELECTOR, self.account_guest).click()



