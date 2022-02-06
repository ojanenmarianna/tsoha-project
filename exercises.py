from db import db

def get_all_exercises():
    sql = "SELECT name FROM exercises ORDER BY user_id"
    return db.session.execute(sql).fetchall()

def add_exercise(name, time, intensity, creator_id):
    #todo add exercise for user
    try:
        sql = """INSERT INTO exercises (name, intensity, time, creator_id)
                VALUES (:name, :intensity, :time, :creator_id)"""
        db.session.execute(sql, {"name": name, "intensity": intensity, "time": time, "cretor_id": creator_id})
        db.session.commit()
    except:
        return False
    return True

