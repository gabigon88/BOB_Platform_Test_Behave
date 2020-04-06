# https://stackoverflow.com/questions/40763066/how-to-generate-reports-in-behave-python

Feature: Check login page item

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
    When I click <link_text>
    Then open new window of <page_url_tag>

    Examples:
      | link_text     | page_url_tag           |
      | 综合App客户端 | https://www.bob16.app/ |
      | 体育App客户端 | https://www.bob11.app/ |
