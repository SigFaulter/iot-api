from flask import Flask, request, jsonify
import os
from api.routes import data, status
from api.db import init_db, db
from api.models.models import Device

def create_api():
    app = Flask(__name__)

    db_path = os.path.join(os.getcwd(), 'instance', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    app.register_blueprint(data.bp)
    app.register_blueprint(status.bp)

    # middleware to verify token
    @app.before_request
    def verify_token():
        given_token = request.headers.get('X-Token-Auth')

        if not given_token:
            return jsonify({'error': 'Missing token'}), 401

        valid_device = Device.query.filter(Device.token == given_token).first()

        if not valid_device:
            return jsonify({'error': 'Invalid token'}), 401

        request.device_id = Device.device_id

    return app

