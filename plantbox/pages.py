from flask import Blueprint, jsonify, render_template

from plantbox.plans import PLANS

pages = Blueprint("pages", __name__)


@pages.get("/")
def home():
    return render_template("home.html")


@pages.route("/box")
def box():
    return render_template("box.html")


@pages.get("/box/plans.json")
def plans_json():
    """The mobile app reads the plans from here."""
    return jsonify(PLANS)