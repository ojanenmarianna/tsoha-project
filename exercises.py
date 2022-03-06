from db import db

def get_all_exercises():
    sql = "SELECT id, name FROM exercises WHERE visible=true ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_my_exercises(user_id):
    sql = "SELECT id, name FROM exercises WHERE creator_id = :user_id AND visible=true ORDER BY name"
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def add_exercise(name, time, intensity, creator_id):
    sql = """INSERT INTO exercises (name, intensity, time, creator_id, visible)
            VALUES (:name, :intensity, :time, :creator_id, true) RETURNING id"""
    exercise_id = db.session.execute(sql, {"name":name, "intensity":intensity, "time":time, "creator_id":creator_id}).fetchone()[0]
    print(exercise_id)
    sql = """INSERT INTO summary (user_id, exercise_id)
        VALUES (:user_id, :exercise_id)"""
    db.session.execute(sql, {"user_id":creator_id, "exercise_id":exercise_id})
    db.session.commit()

    return exercise_id

def get_exercise_info(exercise_id):
    sql = """SELECT e.name, e.time, e.intensity, u.name FROM exercises e, users u
            WHERE e.id = :exercise_id AND e.creator_id = u.id"""
    return db.session.execute(sql, {"exercise_id":exercise_id}).fetchone()

def get_exercise_comments(exercise_id):
    sql = """SELECT u.name, c.comment FROM users u, comments c
            WHERE c.user_id = u.id AND c.exercise_id = :exercise_id ORDER BY c.id"""

    return db.session.execute(sql, {"exercise_id":exercise_id}).fetchall()

def add_comment(exercise_id, user_id, comment):
    sql = """INSERT INTO comments (exercise_id, user_id, sent_at, comment)
        VALUES (:exercise_id, :user_id, NOW(), :comment)"""
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id,
                            "comment":comment})
    db.session.commit()

def remove_exercise(exercise_id):
    sql = "UPDATE exercises SET visible=false WHERE id =:exercise_id"
    db.session.execute(sql, {"exercise_id":exercise_id})
    db.session.commit()
