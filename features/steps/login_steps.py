from behave import *
from utils import ConfigReader


@Given('a user navigates to login page')
def step_impl(context):
    context.driver.get(ConfigReader.read_file("basic_details", "url") + "index.php?rt=account/login")


@When('a user enters a valid credentials')
def step_impl(context):
    context.login_page.login()


@When('a user enters a invalid credentials {username} {password}')
def step_impl(context, username, password):
    context.login_page.login_with_params(username, password)
