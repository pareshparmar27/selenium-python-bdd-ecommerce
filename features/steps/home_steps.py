from behave import *


@Then('a user navigates to the home')
def step_impl(context):
    assert context.home_page.get_header().strip() == "MY ACCOUNT"


@Then('a user gets an error message')
def step_impl(context):
    assert "Error: Incorrect login or password provided." in context.home_page.get_error_message().strip()


@When('a user searches for product {subcategory} under {category}')
def step_impl(context, subcategory, category):
    context.home_page.search(category, subcategory)


@Then('a user gets list of desired {subcategory} product')
def step_impl(context, subcategory):
    assert context.home_page.get_header().strip() == subcategory.upper()
    assert context.home_page.get_product_count() > 0


@When('a user selects a currency as {currency}')
def step_impl(context, currency):
    context.home_page.select_currency(currency)


@Then('a user see the products price in {currency}')
def step_impl(context, currency):
    context.home_page.check_products_currency(currency)
