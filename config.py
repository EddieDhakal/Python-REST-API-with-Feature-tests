import sqlite3


def session():
    return sqlite3.connect('ticket.db')
