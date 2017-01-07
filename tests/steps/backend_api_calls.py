import json

from behave import *
import requests


@when('the ticket is "{status}"')
def _(context, status):
    if context.ticket_id is None:
        assert False

    response = requests.put(
        url=context.base_url + '/change-ticket-status/' + str(context.ticket_id),
        json={'status': status},
        headers={'Content-Type': 'application/json'}
    )
    payload = json.loads(response.text)
    context.ticket_id = payload.get('id')
    assert response.ok
