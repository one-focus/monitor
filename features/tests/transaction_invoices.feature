# Created by kardash at 13.11.21

Feature: TestRail
  # Enter feature description here
  Scenario Outline: Run tests on test rail
    When open url: "https://jenkins.getcurrencies.com/job/tests/job/processing-ui-multibranch-new/job/master/build?delay=0sec"
    Then page testrail is opened
    When enter "alexandr.kardash@coinspaid.com" in login field
    When enter "password" in password field
    When click on login button
    When enter "<test_run_id>" in test run field
    When click on run automated tests button
    When click on ok button

    @transactions
    Examples:
      | test_run_id |
      | 764         |
    @invoices
    Examples:
      | test_run_id |
      | 770         |

