# Created by kardash at 13.11.21

Feature: Coinmarketcap
  # Enter feature description here
  Scenario: monitor coins
    When open url: "https://coinmarketcap.com/new/"
    Then page coinmarketcap is opened
    When get latest coins

