from flask import Blueprint, request, jsonify
from api.db import execute_query

bp = Blueprint('data', __name__, url_prefix='/api/v1/')

# TODO add authentication
# TODO intergrate with db

# Store data of current device
@bp.route('/data', methods=['POST'])
def store_iot_data():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'data is required.'}), 400

    return jsonify({'message': 'Data stored successfully.'}), 201

# Get data of a specific device
@bp.route('/data/<device_id>', methods=['GET'])
def retrieve_iot_data(device_id):
    pass
