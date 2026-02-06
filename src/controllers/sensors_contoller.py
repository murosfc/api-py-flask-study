from src.models.sensor import Sensor
from src.services.sensors_service import SensorsService
from flask import Blueprint, jsonify

sensors_bp = Blueprint('sensors', __name__)

class SensorsController:
    def __init__(self, sensors_service: SensorsService):
        self.sensors_service = sensors_service

    @sensors_bp.route('/', methods=['GET'])
    def get_sensors(self):
        sensors = self.sensors_service.get_sensors()
        return jsonify(sensors)

    @sensors_bp.route('/<string:sensor_id>', methods=['GET'])
    def get_sensor_by_id(self, sensor_id: str):
        try:
            sensor = self.sensors_service.get_sensor_by_id(sensor_id)
            return jsonify(sensor), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @sensors_bp.route('/', methods=['POST'])
    def add_sensor(self, sensor: Sensor):
        try:
            self.sensors_service.add_sensor(sensor)
            return jsonify(sensor.to_dict()), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    @sensors_bp.route('/<string:sensor_id>', methods=['DELETE'])
    def delete_sensor(self, sensor_id: str):
        try:
            self.sensors_service.delete_sensor(sensor_id)
            return jsonify({"message": "Sensor deleted successfully"}), 204
        except ValueError as e:
            return jsonify({"error": str(e)}), 404