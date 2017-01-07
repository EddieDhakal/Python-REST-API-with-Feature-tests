Feature: Create Ticket
  In order to create a Ticket
  As a customer
  I want to let them know the kind of ticket Im creating.

  Scenario: Valid ticket
    Given the customer has issues with "links"
     When created a ticket with "Bug" as a ticket type
      And queried for the ticket status
     Then the ticket should have "Opened" status

  Scenario: Invalid ticket
    Given the customer has issues with "file loaders"
     When created a ticket with "Buggy file loader" as a ticket type
     Then the ticket should not have a Ticket ID
