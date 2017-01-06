Feature: Create Ticket
  In order to create a Ticket
  As a customer
  I want to let them know the kind of ticket Im creating.

  Scenario: Valid ticket
    Given the customer has issues with "links"
     When created a ticket with "Bug" as a ticket type
      And queried for the ticket status
     Then the ticket should have "opened" status
