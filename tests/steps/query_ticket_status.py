from behave import *


@when('queried for the ticket status')
def _(context):
    pass


@then('the ticket should have "{ticket_status}" status')
def _(context, ticket_status):
    pass
