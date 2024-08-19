import sqlite3

def connect_db(db_name='movies.db'):
    return sqlite3.connect(db_name)
