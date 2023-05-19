from selenium import webdriver

from pages.GuestPage import GuestPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage
from utils import ConfigReader


def before_scenario(context, driver):
    match ConfigReader.read_file("basic_details", "browser").upper():
        case "CHROME":
            context.driver = webdriver.Chrome()
        case "FIREFOX":
            context.driver = webdriver.Firefox()
        case "EDGE":
            context.driver = webdriver.Edge()
        case "SAFARI":
            context.driver = webdriver.Safari()
        case default:
            raise ValueError(ConfigReader.read_file("basic_details", "browser") + " browser setup is not yet done...")
    context.driver.maximize_window()
    context.driver.implicitly_wait(ConfigReader.read_file("timeouts", "implicit_wait"))
    context.driver.get(ConfigReader.read_file("basic_details", "url"))
    initialize_pages(context, driver)


def after_scenario(context, driver):
    context.driver.quit()


def initialize_pages(context, driver):
    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)
    context.product_page = ProductPage(context.driver)
    context.guest_page = GuestPage(context.driver)
