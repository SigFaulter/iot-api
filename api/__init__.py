from flask import Flask
import os
from api.routes import data
from api.db import init_db, db

def create_api():
    app = Flask(__name__)

    db_path = os.path.join(os.getcwd(), 'instance', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    app.register_blueprint(data.bp)

    return app

