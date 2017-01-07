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
            ticket = Ticket.create(ticket_type, message)

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


app = falcon.API()
app.add_route('/create-ticket', CreateTicket)
