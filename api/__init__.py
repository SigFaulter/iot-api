from flask import Flask
import os
from api.db import db
from api.routes import data

def create_api():
    app = Flask(__name__)

    db_path = os.path.join(os.getcwd(), 'instance', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register routes
    app.register_blueprint(data.bp)

    return app
