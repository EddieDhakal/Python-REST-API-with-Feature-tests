import threading
from wsgiref import simple_server

from handlers import app
from config import session
from repo import Repo


def clear_database():
    with session() as db:
        repo = Repo(db)
        repo.clear_database()
        db.commit()


def before_all(context):
    context.host = 'localhost'
    context.port = 8000
    context.base_url = 'http://' + context.host + ':' + str(context.port)
    context.server = simple_server.make_server(
        host=context.host,
        port=context.port,
        app=app
    )
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()


def after_all(context):
    clear_database()
    context.server.shutdown()
    context.thread.join()
