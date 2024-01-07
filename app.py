from flask import Flask
import os
from application.models import *
from application import config
from application.config import LocalConfig

app = None


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    db.init_app(app)
    app.app_context().push()
    return app


app = create_app()

from application import controllers


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
