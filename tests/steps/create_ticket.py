import json

from behave import *
import requests


@given('the customer has issues with "{issue}"')
def _(context, issue):
    pass


@when('created a ticket with "{issue_type}" as a ticket type and message "{message}"')
def _(context, issue_type, message):
    request_payload = {
        "ticket_type": issue_type,
        "message": message
    }

    response = requests.post(
        url=context.base_url + '/create-ticket',
        json=request_payload,
        headers={'Content-Type': 'application/json'}
    )

    response_payload = json.loads(response.text)
    context.ticket_id = response_payload.get('id')
    context.error = response_payload.get('reason')
    assert response.ok


@then('the ticket should have an ID')
def _(context):
    assert type(context.ticket_id) == int


@then('the system should respond saying "{issue_type}" is not a valid ticket type')
def _(context, issue_type):
    assert context.ticket_id is None
    assert issue_type in context.error
