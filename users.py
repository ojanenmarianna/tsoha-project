import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
    sql = "SELECT password, id, role FROM users WHERE name=:name"
    result = db.session.execute(sql, {"name":name})
    user = result.fetchone()
    
    if not user:
        return False
    
    if not check_password_hash(user[0], password):
        return False
        
    session["user_id"] = user[1]
    session["user_name"] = name
    session["user_role"] = user[2]
    session["csrf_token"] = os.urandom(16).hex()
    return True

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]

def register(name, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (name, password, role, visible)
                 VALUES (:name, :password, :role, true)"""
        db.session.execute(sql, {"name":name, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return login(name, password)

def user_id():
    return session.get("user_id", 0)

def user_role():
    return session.get("user_role", 0)

def require_role(role):
    if role > session.get("user_role", 0):
        abort(403)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def get_all_users():
    sql = "SELECT id, name FROM users WHERE visible=true ORDER BY name"
    return db.session.execute(sql).fetchall()

def remove_user(user_id):
    sql = "UPDATE users SET VISIBLE=false WHERE id =:user_id"
    db.session.execute(sql, {"user_id":user_id})
    db.session.commit()