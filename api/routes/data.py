from flask import Blueprint, request, jsonify
from api.models.models import Data
from api.db import db

bp = Blueprint('data', __name__, url_prefix='/api/v1/')

# TODO add authentication

# Store data of current device
@bp.route('/data', methods=['POST'])
def store_iot_data():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'data is required.'}), 400

    try:
        db.session.commit()
        return jsonify({'message': 'Data stored successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get all data from current device
@bp.route('/data', methods=['GET'])
def retrive_all_iot_data():
    data = Data.query.all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        db.session.commit()
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get data from a specific row onwards
@bp.route('/data/<int:id>', methods=['GET'])
def retrieve_iot_data(id):
    data = Data.query.filter(Data.id >= id).all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        db.session.commit()
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
