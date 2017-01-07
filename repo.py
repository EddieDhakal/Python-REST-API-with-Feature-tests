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
