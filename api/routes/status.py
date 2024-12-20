from flask import Blueprint, request, jsonify
from api.models.models import Status

bp = Blueprint('status', __name__, url_prefix='/api/v1/')

# TODO add authentication

# Get current status the iot should adhere to
@bp.route('/status', methods=['GET'])
def get_status():
    data = Status.query.all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    return jsonify({'data': [d.to_dict() for d in data]}), 200

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

    return jsonify({'message': 'Status updated successfully.'}), 201
