import json

from behave import *
import requests


@given('the customer has issues with "{issue}"')
def _(context, issue):
    pass


@when('created a ticket with "{issue_type}" as a ticket type')
def _(context, issue_type):
    request_payload = {
        "ticket_type": "Bug",
        "message": "The links are broken."
    }

    response = requests.post(
        url=context.base_url + '/create-ticket',
        json=request_payload,
        headers={'Content-Type': 'application/json'}
    )

    response_payload = json.loads(response.text)
    context.ticket_id = response_payload.get('id')
    assert type(context.ticket_id) is int
    assert response.ok
