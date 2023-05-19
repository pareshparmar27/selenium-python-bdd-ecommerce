from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GuestPage(BasePage):
    firstname = '#guestFrm_firstname'
    lastname = '#guestFrm_lastname'
    email = '#guestFrm_email'
    address_one = '#guestFrm_address_1'
    city = '#guestFrm_city'
    state = '#guestFrm_zone_id'
    zipcode = '#guestFrm_postcode'
    country = '#guestFrm_country_id'

    def __init__(self, driver):
        super().__init__(driver)

    def add_details(self):
        self.enter_personal_details()
        self.enter_address()

    def enter_personal_details(self):
        self.driver.find_element(By.CSS_SELECTOR, self.firstname).send_keys("Paresh")
        self.driver.find_element(By.CSS_SELECTOR, self.lastname).send_keys("Parmar")
        self.driver.find_element(By.CSS_SELECTOR, self.email).send_keys("test@testme.com")

    def enter_address(self):
        self.driver.find_element(By.CSS_SELECTOR, self.address_one).send_keys("Test Street")
        self.driver.find_element(By.CSS_SELECTOR, self.city).send_keys("Test City")
        select_country = Select(self.driver.find_element(By.CSS_SELECTOR, self.country))
        select_country.select_by_visible_text("Austria")
        select_state = Select(self.driver.find_element(By.CSS_SELECTOR, self.state))
        select_state.select_by_visible_text("Tirol")
        self.driver.find_element(By.CSS_SELECTOR, self.zipcode).send_keys("412101")
        self.click_button("Continue")
