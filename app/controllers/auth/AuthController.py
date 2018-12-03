from flask import request, render_template, session, redirect
from app import app

from app.models.auth.Auth import Auth

from app.models.User import User

#verifyng login user
@app.route("/auth/login/", methods=["POST"])
def auth_login():
    email = request.form.get("email")
    password = request.form.get("password")

    result = Auth().login(email=email, password=password)

    if result:
        user = User().getUserByEmail(email)

        session["_id"] = str(user["_id"])
        session["email"] = user["email"]

        return redirect("/coaprendiz/")
    else:
        return render_template("login.html", error="E-mail ou senha inválidos!")

#registering new user
@app.route("/auth/signup/", methods=["POST"])
def auth_signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    return "OK"

#logout user
@app.route("/coaprendiz/logout/", methods=["GET"])
def logout():
    session.pop("email", None)
    session.pop("_id", None)
    return redirect("/coaprendiz/")
