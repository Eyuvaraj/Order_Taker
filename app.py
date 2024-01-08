from flask import Flask
from application.models import *
from application import config
from application.config import LocalConfig
from application.controllers.admin import admin
from application.controllers.user import user

app = None


def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    db.init_app(app)
    app.app_context().push()
    app.secret_key = "4321-4342-7574-2412"
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(user, url_prefix="/user")
    return app


app = create_app()

from application.index import *

if __name__ == "__main__":
    app.run(debug=True)
