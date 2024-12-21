from flask import Blueprint, request, jsonify
from api.models.models import Status
from api.db import db

bp = Blueprint('status', __name__, url_prefix='/api/v1/')

# TODO add authentication

# Get current status the iot should adhere to
@bp.route('/status', methods=['GET'])
def get_status():
    data = Status.query.all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        return jsonify({'data': [d.to_dict() for d in data]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Set the status that the device should be in
@bp.route('/status/<string:device_id>', methods=['PUT'])
def set_status(device_id):
    data = request.get_json()
    status = Status.query.get(Status.device_id == device_id)

    if not data:
        return jsonify({'error': 'Status of this device not found.'}), 404

    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)

    try:
        db.session.commit()
        return jsonify({'message': 'Status updated successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
