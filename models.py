class Ticket:

    TICKETS_TYPES = {
        'Proposal': 1,
        'Task': 2,
        'Bug': 4
    }

    STATUSES = {
        'Opened': 1,
        'Closed': 2
    }

    default_status = STATUSES.get('Opened')

    @classmethod
    def find_status_name(cls, status_id):
        """
        Finds the status name for a given status ID.
        """
        statuses = cls.STATUSES
        reversed_statuses = dict(zip(statuses.values(), statuses.keys()))
        return reversed_statuses.get(status_id)

    @classmethod
    def create(cls, ticket_type, message):
        """
        Creates a new ticket.

        :param ticket_type: Proposal, Task or Bug
        :param message: Text describing the ticket
        :return: A ticket object
        """
        default_status_name = cls.find_status_name(cls.default_status)
        return cls(
            ticket_type=ticket_type,
            status=default_status_name,
            message=message
        )

    def __init__(self, message, ticket_type, ticket_id=0, status=default_status):
        """
        Please note: We do not know the ticket ID yet until it is saved in the database.
        `ticket_id=0` indicates the ticket is still in the memory not been saved yet.

        :param message: Text describing the ticket
        :param ticket_type: Proposal, Task or Bug
        :param ticket_id: Ticket ID as in the database
        :param status: Opened or Closed
        """
        # The IDE complains for not following the PEP8 naming convention
        #   if I do not initialize the instant variables to None
        self._status = None
        self._message = None
        self._ticket_type = None

        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.status = status
        self.message = message

    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, new_ticket_type):
        if new_ticket_type not in Ticket.TICKETS_TYPES:
            raise ValueError(new_ticket_type + ' is not a valid ticket type.')
        self._ticket_type = new_ticket_type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in Ticket.STATUSES:
            raise ValueError(new_status + ' is not a valid status.')

        if self.status == new_status:
            return

        if hasattr(self, 'status'):
            self._status = new_status
        else:
            raise ValueError('Status is not a defined.')

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, new_message):
        if len(new_message) < 12:
            raise ValueError('Message must be of 12 characters or longer.')
        self._message = new_message
