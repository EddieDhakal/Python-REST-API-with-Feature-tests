import json

import falcon

from models import Ticket
from config import session
from repo import Repo


class CreateTicket:

    @staticmethod
    def on_post(req, resp):
        request_payload = json.loads(req.stream.read().decode('utf-8'))
        ticket_type = request_payload.get('ticket_type')
        message = request_payload.get('message')

        try:
            ticket = Ticket.create_new(ticket_type, message)

            with session() as db:
                repo = Repo(db)
                ticket.ticket_id = repo.save_new_ticket(ticket)
                db.commit()

            resp.body = json.dumps(
                {
                    'id': ticket.ticket_id,
                    'status': ticket.status
                },
                sort_keys=True, indent=4
            )
        except ValueError as error:
            resp.body = json.dumps(
                {
                    'status': 'failed',
                    'reason': str(error)
                },
                sort_keys=True, indent=4
            )


class QueryTicketStatus:

    @staticmethod
    def on_get(req, resp, ticket_id):
        with session() as db:
            repo = Repo(db)
            ticket = repo.list_ticket(int(ticket_id))

        if ticket is None:
            resp.body = json.dumps({'status': 'not found'}, sort_keys=True, indent=4)
        else:
            resp.body = json.dumps(
                {
                    'id': ticket.ticket_id,
                    'ticket_type': ticket.ticket_type,
                    'status': Ticket.find_status_name(ticket.status)
                },
                sort_keys=True, indent=4
            )

app = falcon.API()
app.add_route('/create-ticket', CreateTicket)
app.add_route('/view-status/{ticket_id}', QueryTicketStatus)
