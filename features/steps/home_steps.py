from behave import *


@Then('a user navigates to the home')
def step_impl(context):
    assert context.home_page.get_header().strip() == "MY ACCOUNT"


@Then('a user gets an error message')
def step_impl(context):
    assert "Error: Incorrect login or password provided." in context.home_page.get_error_message().strip()