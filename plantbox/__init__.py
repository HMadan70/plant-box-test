"""Plant Box: Leaf & Pot's monthly plant subscription."""

from flask import Flask

from plantbox import db
from plantbox.pages import pages


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(DATABASE="plantbox.sqlite", ADMIN_PASSWORD="change-me")
    app.config.update(config or {})
    db.init_db(app.config["DATABASE"])
    app.register_blueprint(pages)
    return app
