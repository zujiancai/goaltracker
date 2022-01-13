# http://flask.pocoo.org/docs/1.0/tutorial/database/
# https://www.arangodb.com/tutorials/tutorial-python/

from flask import g
import os
from pyArango.connection import *

# Configuration
ARANGODB_HOST = os.environ.get("GTR_ARANGODB_HOST", "http://127.0.0.1:8529")
ARANGODB_ROOT_PWD = os.environ.get("GTR_ARANGODB_ROOT_PWD", "")
DATABASE_NAME = "GoalTracker"


def get_db():
    if "db" not in g:
        conn = Connection(arangoURL=ARANGODB_HOST, username="root", password=ARANGODB_ROOT_PWD)
        if conn.hasDatabase(DATABASE_NAME):
            g.db = conn[DATABASE_NAME]
        else:
            g.db = conn.createDatabase(name=DATABASE_NAME)

    return g.db


def close_db(e=None):
    db = g.pop("db", None)


def init_app(app):
    app.teardown_appcontext(close_db)