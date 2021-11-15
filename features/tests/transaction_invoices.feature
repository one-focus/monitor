# Created by kardash at 13.11.21

Feature: TestRail
  # Enter feature description here
  Scenario Outline: Run tests on test rail
    When open url: "<url>"
    Then page testrail is opened
    When enter "alexandr.kardash@coinspaid.com" in login field
    When enter "password" in password field
    When click on login button
    When click on run automated tests button
    When click on ok button

    @transactions
    Examples:
      | url                                                         |
      | https://testrail.getcurrencies.com/index.php?/runs/view/764 |
    @invoices
    Examples:
      | url                                                         |
      | https://testrail.getcurrencies.com/index.php?/runs/view/770 |

