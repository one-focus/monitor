# Created by kardash at 13.11.21

Feature: Visa
  # Enter feature description here
  @visa
  Scenario: Run tests on test rail
    When open url: "https://it.tlscontact.com/by/msq/myapp.php?fg_id=937068"
    Then page italy visa is opened
    When login visa
    When monitor visa