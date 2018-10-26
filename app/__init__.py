from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coaprendiz/login/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/coaprendiz/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/coaprendiz/settings/", methods=["GET"])
def settings():
    return render_template("settings.html")


@app.route("/coaprendiz/signup/1/", methods=["GET"])
def signup1():
    return render_template("signup1.html")


@app.route("/coaprendiz/signup/2/", methods=["GET"])
def signup2():
    return render_template("signup2.html")


