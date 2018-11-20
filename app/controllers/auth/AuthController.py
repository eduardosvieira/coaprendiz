from flask import request
from app import app

#verifyng login user
@app.route("/auth/login/", methods=["POST"])
def auth_login():
    email = request.form.get("email")
    password = request.form.get("password")

    print(email)
    print(password)

    return "OK"

#registering new user
@app.route("/auth/signup/", methods=["POST"])
def auth_signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    return "OK"
