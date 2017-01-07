Feature: Query Ticket Status
  As a customer Im desperate to know what is
  happening to the ticket I just created.

  Scenario: Query my ticket
    When created a ticket with "Proposal" as a ticket type and message "Would love support Blackberry mobiles."
     And queried for the ticket status
    Then the ticket should have "Opened" status
    When the ticket is "Closed"
     And queried for the ticket status
    Then the ticket should have "Closed" status
