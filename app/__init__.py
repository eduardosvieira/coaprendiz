from flask import Flask, render_template

app = Flask(__name__)

#defining route to index
@app.route("/coaprendiz/", methods=["GET"])
def index():
    return render_template("index.html")


#defining route to login
@app.route("/coaprendiz/login/", methods=["GET"])
def login():
    return render_template("login.html")


#defining route to settings
@app.route("/coaprendiz/settings/", methods=["GET"])
def settings():
    return render_template("settings.html")


#defining route to signup
@app.route("/coaprendiz/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")
