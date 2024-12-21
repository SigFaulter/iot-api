from flask import Blueprint, request, jsonify
from api.models.models import Data
from api.db import db

bp = Blueprint('data', __name__, url_prefix='/api/v1/')

# Store data of current device
@bp.route('/data', methods=['POST'])
def store_iot_data():
    device_id = request.device_id

    temperature = request.json.get('temperature')
    humidity = request.json.get('humidity')
    leds_stats = request.json.get('leds_stats')
    servo = request.json.get('servo')
    brightness = request.json.get('brightness')

    if not all([temperature, humidity, leds_stats, servo, brightness]):
        return jsonify({'error': 'Missing required fields.'}), 400

    data_dict = {
        'device_id': device_id,
        'temperature': temperature,
        'humidity': humidity,
        'leds_stats': leds_stats,
        'servo': servo,
        'brightness': brightness
    }

    try:
        new_data = Data(**data_dict)

        db.session.add(new_data)
        db.session.commit()

        return jsonify({'message': 'Data stored successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get all data from current device
@bp.route('/data', methods=['GET'])
def retrieve_all_iot_data():
    data = Data.query.filter(Data.device_id == request.device_id).all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
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
        data = Data.query.filter(Data.device_id == request.device_id).order_by(Data.id.desc()).first()
        if not data:
            return jsonify({'error': 'No data found for this device.'}), 404
        return jsonify({'data': data.to_dict()}), 200
    else:
        data = Data.query.filter(Data.device_id == request.device_id and data.id >= id).all()

        if not data:
            return jsonify({'error': 'No data found for this device.'}), 404

    try:
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
