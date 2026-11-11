from flask import Blueprint, render_template

pages = Blueprint("pages", __name__)


@pages.get("/")
def home():
    return render_template("home.html")
