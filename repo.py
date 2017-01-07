from models import Ticket


class Repo:
    def __init__(self, db):
        self.db = db

    def clear_database(self):
        self.db.execute('delete from tickets')
        self.db.execute('vacuum')

    def save_new_ticket(self, ticket):
        data = (
            Ticket.TICKETS_TYPES[ticket.ticket_type],
            ticket.status,
            ticket.message
        )

        cursor = self.db.execute("""
            insert into tickets (ticket_type, status, message)
            values (?, ?, ?)
        """, data)
        return cursor.lastrowid

    def list_ticket(self, ticket_id):
        cursor = self.db.execute("""
            SELECT id, ticket_type, status, message
            FROM tickets
            WHERE id = ?
        """, (str(ticket_id),))
        tickets = cursor.fetchall()

        if len(tickets) == 1:
            ticket = tickets[0]
            return Ticket(
                ticket_id=ticket[0],
                ticket_type=Ticket.find_ticket_name(ticket[1]),
                status=ticket[2],
                message=ticket[3]
            )
