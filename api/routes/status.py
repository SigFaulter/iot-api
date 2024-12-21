from flask import Blueprint, request, jsonify
from api.models.models import Status
from api.db import db

bp = Blueprint('status', __name__, url_prefix='/api/v1/')

# Get current status the iot should adhere to
@bp.route('/status', methods=['GET'])
def get_status():
    data = Status.query.filter(request.device_id == Status.device_id).first()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    try:
        return jsonify(data.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Set the status that the device should be in
@bp.route('/status', methods=['PUT', 'PATCH'])
def set_status():
    status = Status.query.filter(Status.device_id == request.device_id).first()

    if not status:
        return jsonify({'error': 'Status of this device not found.'}), 404


    try:
        status.leds_stats = request.json.get("leds_stats")
        status.servo = request.json.get("servo")
        db.session.commit()
        return jsonify({'message': 'Status updated successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
