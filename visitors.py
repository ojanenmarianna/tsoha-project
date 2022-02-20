import os
from db import db

def count_visits():
    sql = "SELECT COUNT(*) FROM visitors"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def add_visit():
    sql = "INSERT INTO visitors (time) VALUES (NOW())"
    db.session.execute(sql)
    db.session.commit()