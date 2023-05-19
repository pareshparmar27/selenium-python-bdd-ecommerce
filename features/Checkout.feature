Feature: Product Checkout Test

  @checkout @regression @register-account
  Scenario: Order a shampoo product with registered account
    When a user searches for product Shampoo under HAIR CARE
    Then a user can order a product with registered account

  @checkout @regression @guest-account
  Scenario: Order a eyes product with guest account
    When a user searches for product Eyes under SKINCARE
    Then a user can order a product with guest account