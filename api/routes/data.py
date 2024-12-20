from flask import Blueprint, request, jsonify
from api.db import db
from api.models.models import Data

bp = Blueprint('data', __name__, url_prefix='/api/v1/')

# TODO add authentication

# Store data of current device
@bp.route('/data', methods=['POST'])
def store_iot_data():
    
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'data is required.'}), 400

    return jsonify({'message': 'Data stored successfully.'}), 201

# Get data of 
@bp.route('/data/<int:id>', methods=['GET'])
def retrieve_iot_data(id):
    # Filter data from id to newer rows
    data = Data.query.filter(Data.id >= id).all()

    if not data:
        return jsonify({'error': 'No data found for this device.'}), 404

    result = [{'result': d.data} for d in data]
    return jsonify(result), 200
