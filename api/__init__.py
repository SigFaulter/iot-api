from flask import Flask
from .models import db
from .routes import data

def create_api():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register blueprints
    app.register_blueprint(data.bp)

    return app

