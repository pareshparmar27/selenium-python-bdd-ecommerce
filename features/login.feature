Feature: Login Test

  Scenario: Successfully login
    Given a user navigates to login page
    When  a user enters a valid credentials
    Then  a user navigates to the home


  Scenario Outline: Unsuccessfully login
    Given a user navigates to login page
    When  a user enters a invalid credentials <username> <password>
    Then  a user gets an error message
    Examples:
      | username    | password        |
      | invaliduser | password        |
      | username    | invalidpassword |