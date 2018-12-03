from flask import Flask, render_template, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "@secret"

from app.controllers.auth import AuthController
from app.controllers import User
from app.models.User import User

from app.models.Help import Help

#defining route to index
@app.route("/coaprendiz/", methods=["GET"])
def index():
    if "_id" in session:
        user = User().getUserByEmail(session["email"])

        return render_template("app.html", user=user)
    else:
        return render_template("index.html")


#defining route to login
@app.route("/coaprendiz/login/", methods=["GET"])
def login():
    if "_id" in session:
        return redirect("/coaprendiz/")
    else:
        return render_template("login.html")


#defining route to settings
@app.route("/coaprendiz/settings/", methods=["GET"])
def settings():
    return render_template("settings.html")


#defining route to signup
@app.route("/coaprendiz/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")
