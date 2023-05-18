Feature: Login Test

  Background: login page
    Given a user navigates to login page

  @login @successful @regression @smoke
  Scenario: Successfully login
    When  a user enters a valid credentials
    Then  a user navigates to the home

  @login @unsuccessful @regression @smoke
  Scenario Outline: Unsuccessfully login
    When  a user enters a invalid credentials <username> <password>
    Then  a user gets an error message
    Examples:
      | username    | password        |
      | invaliduser | password        |
      | username    | invalidpassword |