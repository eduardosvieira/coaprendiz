from flask import render_template, session

from app import app

from app.models.User import User
from app.models.Help import Help

@app.route("/coaprendiz/<user_id>/")
def get_profile_page(user_id):
    if "_id" in session:
        if session["_id"] == user_id:
            user = User().getUserByEmail(session["email"])
            helps = Help().getHelpsByUser(session["email"])

            return render_template("profile-page.html", user=user, helps=helps)

    return redirect("/coaprendiz/login/")
