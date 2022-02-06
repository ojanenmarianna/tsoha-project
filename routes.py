from app import app
from flask import render_template, request, redirect
import users
import exercises

#Add exercise
@app.route("/add", methods=["get", "post"])
def add_exercise():
    if request.method == "GET":
        return render_template("add.html")
    
    if request.method == "POST":
        users.check_csrf()
        creator_id = users.user_id()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Nimessä tulee olla 1-20 merkkiä")

        time = request.form["time"]
        if time < 1:
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
        return redirect("/frontpage")

#Home page
@app.route("/frontpage")
def frontpage():
    return render_template("frontpage.html")

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
        return redirect("/frontpage")

#Logout
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")