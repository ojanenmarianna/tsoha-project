from app import app
from flask import render_template, request, redirect
import users
import exercises
import visitors

#Add exercise
@app.route("/add", methods=["get", "post"])
def add_exercise():
    users.require_role(1 or 2)
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        users.check_csrf()

        creator_id = users.user_id()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Harjoituksen nimessä tulee olla 1-20 merkkiä")

        time = request.form["time"]
        if int(time) < 1:
            return render_template("error.html", message="Keston tulee olla vähintään 1 minuutti")

        intensity = request.form["intensity"]
        if intensity not in ("1", "2", "3"):
            return render_template("error.html", message="Tuntematon intensiteetti")
        
        if not exercises.add_exercise(name, time, intensity, creator_id):
            return render_template("error.html", message="Harjoitusta ei lisätty")
        return redirect("/frontpage")
        

#Login page
@app.route("/", methods=["get", "post"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Väärä tunnus tai salasana")
        visitors.add_visit()
        return redirect("/frontpage")

#Show exercise
@app.route("/exercise/<int:exercise_id>")
def show_exercise(exercise_id):
    info = exercises.get_exercise_info(exercise_id)
    #todo get comment for exercise

    return render_template("exercise.html", id=exercise_id, name=info[0], creator=info[3], time=info[1], intensity=info[2])

#Add comment to exercise
@app.route("/comment", methods=["post"])
def comment():

    exercise_id = request.form["exercise_id"]
    comment = request.form["comment"]

    exercises.add_comment(exercise_id, users.user_id(), comment)
    
    return redirect("/exercise/"+str(exercise_id))

#Home page
@app.route("/frontpage")
def frontpage():
    all_exercises = exercises.get_all_exercises()
    my_exercises = exercises.get_my_exercises(users.user_id())
    visits = visitors.count_visits()
    return render_template("frontpage.html", count=len(all_exercises), exercises=all_exercises, my_count=len(my_exercises), my_exercises=my_exercises, counter=visits)

#Register page
@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 2 or len(username) > 20:
            return render_template("error.html", message="Tunnuksessa tulee olla 2-20 merkkiä")

        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if password1 == "":
            return render_template("error.html", message="Salasana tyhjä")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if not users.register(username, password1, role):
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        return redirect("/")

#Logout
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")