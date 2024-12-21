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
def retrieve_all_iot_data():
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
# any negative number == last row available
@bp.route('/data/<id>', methods=['GET'])
def retrieve_iot_data(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({'error': 'Invalid ID format'}), 400

    if id < 0:
        data = Data.query.order_by(Data.id.desc()).first()
        if not data:
            return jsonify({'error': 'No data found for this device.'}), 404
        return jsonify({'data': data.to_dict()}), 200
    else:
        data = Data.query.filter(Data.id >= id).all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        db.session.commit()
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
