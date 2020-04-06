# https://stackoverflow.com/questions/40763066/how-to-generate-reports-in-behave-python

Feature: Test login page

  Scenario: click register page button
    Given I open login page
    When I click register page button
    Then page is register page

  Scenario: click login page button
    Given I open login page
    When I click register page button
    When I click login page button
    Then page is login page

  Scenario Outline: click show password button
    Given I open login page
    When I input <password> in password field
    When I click show password button
    Then the <password> is visible

    Examples:
      | password   | !notes            |
      | ABCDE12345 | password template |


  Scenario: click forgot password
    Given I open login page
    When I click forgot password
    Then page is forgot password page


  Scenario Outline: click download hyperlink
    Given I open login page
    When I click <link_text> link
    Then open new window of <page_url_tag>

    Examples:
      | link_text     | page_url_tag           |
      | 综合App客户端 | https://www.bob16.app/ |
      | 体育App客户端 | https://www.bob11.app/ |


  Scenario Outline: user login
    Given I open login page
    When I input <account> in account field
    When I input <password> in password field
    When I click login button
    Then home page userName is <account>

    Examples:
      | account   | password   |
      | ggwp12345 | abcde12345 |
