from flask import request
from app import app

from app.models.auth.Auth import Auth

#verifyng login user
@app.route("/auth/login/", methods=["POST"])
def auth_login():
    email = request.form.get("email")
    password = request.form.get("password")

    result = Auth().login(email=email, password=password)

    print(result)

    return "OK"

#registering new user
@app.route("/auth/signup/", methods=["POST"])
def auth_signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    return "OK"
