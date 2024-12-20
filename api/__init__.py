from flask import Flask
from api.db import db
from api.routes import data

def create_api():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register routes
    app.register_blueprint(data.bp)

    return app
