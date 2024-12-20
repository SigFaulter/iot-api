import sqlite3

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('app.db')
        db.row_factory = sqlite3.Row
    return db

def execute_query(query, args=(), commit=False):
    db = get_db()
    cursor = db.execute(query, args)
    if commit:
        db.commit()
    return cursor

def close_db(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

