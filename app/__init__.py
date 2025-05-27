from flask import Flask
from .routes.user_routes import user_bp


def create_app():
    app = Flask(__name__)

    # Register Blueprint
    app.register_blueprint(user_bp, url_prefix='/users')

    return app
