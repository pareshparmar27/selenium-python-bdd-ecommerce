Feature: Home Test

  @home @regression @search
  Scenario Outline: Search <sub-category> under <category> category
    When  a user searches for product <sub-category> under <category>
    Then  a user gets list of desired <sub-category> product
    Examples:
      | category              | sub-category  |
      | APPAREL & ACCESSORIES | Shoes         |
      | MAKEUP                | Eyes          |
      | SKINCARE              | Sun           |
      | FRAGRANCE             | Women         |
      | MEN                   | Body & Shower |
      | HAIR CARE             | Shampoo       |
      | BOOKS                 | Audio CD      |

  @home @regression @currency
  Scenario Outline: Show the products price in <currency> currency
    When a user selects a currency as <currency>
    Then a user see the products price in <currency>
    Examples:
      | currency       |
      | Euro           |
      | US Dollar      |
      | Pound Sterling |