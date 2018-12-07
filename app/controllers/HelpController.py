from flask import request, redirect, session
from app import app

from app.models.User import User
from app.models.Help import Help

@app.route("/coaprendiz/helps/", methods=["POST"])
def create_help():
    title = request.form.get("title")
    description = request.form.get("description")
    topics = request.form.get("topics")
    skills = request.form.get("skills")

    user = User().getUserByEmail(session["email"])

    help = Help(title=title, description=description, topics=topics, user=user, skills=skills)

    help.create(help)

    return redirect("/coaprendiz/")
