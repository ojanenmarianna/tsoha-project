from db import db

def get_all_exercises():
    sql = "SELECT id, name FROM exercises ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_my_exercises(user_id):
    sql = "SELECT id, name FROM exercises WHERE creator_id = :user_id ORDER BY name"
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def add_exercise(name, time, intensity, creator_id):
    #todo add exercise for user
    sql = """INSERT INTO exercises (name, intensity, time, creator_id)
            VALUES (:name, :intensity, :time, :creator_id)"""
    db.session.execute(sql, {"name": name, "intensity": intensity, "time": time, "creator_id": creator_id})
    db.session.commit()

    return True

def get_exercise_info(exercise_id):
    sql = """SELECT e.name, e.time, e.intensity, u.name FROM exercises e, users u
            WHERE e.id = :exercise_id AND e.creator_id = u.id"""
    return db.session.execute(sql, {"exercise_id": exercise_id}).fetchone()

def add_comment(exercise_id, user_id, comment):
    sql = """INSERT INTO comments (exercise_id, user_id, sent_at, comment)
        VALUES (:exercise_id, :user_id, NOW(), :comment)"""
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id,
                            "comment":comment})
    db.session.commit()