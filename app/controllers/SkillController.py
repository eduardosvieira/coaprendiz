from flask import jsonify
from app import app

from app.models.Skill import Skill

@app.route("/coaprendiz/skills/", methods=["GET"])
def get_skills():
    result = Skill().getAllSkills()

    skills = []

    for s in result:
        s["_id"] = str(s["_id"])

        skills.append(s)

    return jsonify(skills)
