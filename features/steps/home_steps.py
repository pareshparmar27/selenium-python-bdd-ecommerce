from behave import *


@Then('a user navigates to the home')
def step_impl(context):
    assert context.home_page.get_header().text.strip() == "MY ACCOUNT"


@Then('a user gets an error message')
def step_impl(context):
    assert "Error: Incorrect login or password provided." in context.home_page.get_error_message().strip()


@When('a user searches for product {subcategory} under {category}')
def step_impl(context, subcategory, category):
    context.home_page.search(category, subcategory)


@Then('a user gets list of desired {subcategory} product')
def step_impl(context, subcategory):
    assert context.home_page.get_header().text.strip() == subcategory.upper()
    assert context.home_page.get_product_count() > 0


@When('a user selects a currency as {currency}')
def step_impl(context, currency):
    context.home_page.select_currency(currency)


@Then('a user see the products price in {currency}')
def step_impl(context, currency):
    context.home_page.check_products_currency(currency)


@Then('a user can order a product with registered account')
def step_impl(context):
    context.product_page.get_cart()[0].click()
    context.home_page.click_button("Checkout")
    context.login_page.select_account("Register")
    context.login_page.login_with_params("username", "password")
    context.home_page.click_button("Confirm Order")
    context.home_page.wait_until_text_visibility(context.home_page.header, "YOUR ORDER HAS BEEN PROCESSED!")
    assert "YOUR ORDER HAS BEEN PROCESSED!" in context.home_page.get_header().text.strip()


@Then('a user can order a product with guest account')
def step_impl(context):
    context.product_page.get_cart()[0].click()
    context.home_page.click_button("Checkout")
    context.login_page.select_account("Guest")
    context.login_page.click_button("Continue")
    context.guest_page.add_details()
    context.home_page.click_button("Confirm Order")
    context.home_page.wait_until_text_visibility(context.home_page.header, "YOUR ORDER HAS BEEN PROCESSED!")
    assert "YOUR ORDER HAS BEEN PROCESSED!" in context.home_page.get_header().text.strip()