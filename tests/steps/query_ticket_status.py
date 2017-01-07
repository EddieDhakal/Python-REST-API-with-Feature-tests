import json

from behave import *
import requests


@when('queried for the ticket status')
def _(context):
    response = requests.get(
        url=context.base_url + '/view-status/' + str(context.ticket_id),
        headers={'Content-Type': 'application/json'}
    )
    payload = json.loads(response.text)
    context.ticket_status = payload.get('status')
    assert response.ok


@then('the ticket should have "{ticket_status}" status')
def _(context, ticket_status):
    assert context.ticket_status == ticket_status


@then('the ticket should not have a Ticket ID')
def _(context):
    assert context.ticket_id is None
