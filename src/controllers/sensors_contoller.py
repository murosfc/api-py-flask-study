from flask import Blueprint, jsonify, request
from src.services.sensors_service import SensorsService
from src.repositories.sensors_repository import SensorRepository
from src.models.sensor import Sensor

# Create blueprint
sensors_bp = Blueprint('sensors', __name__)

# Initialize dependencies (singleton pattern for stateless serverless)
sensor_repository = SensorRepository()
sensors_service = SensorsService(sensor_repository)

@sensors_bp.route('/', methods=['GET'])
def get_sensors():
    """Get all sensors (filtered, no null values)"""
    try:
        sensors = sensors_service.get_sensors()
        return jsonify(sensors), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sensors_bp.route('/<string:sensor_id>', methods=['GET'])
def get_sensor_by_id(sensor_id):
    """Get sensor by ID"""
    try:
        sensor = sensors_service.get_sensor_by_id(sensor_id)
        return jsonify(sensor), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sensors_bp.route('/', methods=['POST'])
def add_sensor():
    """Add new sensor"""
    try:
        data = request.get_json()
        
        if not data or 'id' not in data:
            return jsonify({"error": "Missing required field: id"}), 400
        
        sensor = Sensor(
            id=data.get('id'),
            value=data.get('value'),
            timestamp=data.get('timestamp')
        )
        
        result = sensors_service.add_sensor(sensor)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sensors_bp.route('/<string:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    """Delete sensor"""
    try:
        result = sensors_service.delete_sensor(sensor_id)
        return jsonify({"message": f"Sensor {sensor_id} deleted successfully", "sensor": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500