class Repo:
    def __init__(self, db):
        self.db = db

    def clear_database(self):
        self.db.execute('delete from tickets')
        self.db.execute('vacuum')
