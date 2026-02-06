from src.models.sensor import Sensor
from src.repositories.sensors_repository import SensorRepository

class SensorsService:
    def __init__(self, sensor_repository: SensorRepository):
        self.sensor_repository = sensor_repository
  
    def get_sensors(self):
        sensors = self.sensor_repository.get_sensors()
        filtered_sensors = [sensor for sensor in sensors if sensor.value is not None]
        return filtered_sensors

    def get_sensor_by_id(self, sensor_id: str):
        sensor = self.sensor_repository.get_sensor_by_id(sensor_id) 
        if not sensor:
            raise ValueError(f"Sensor with id {sensor_id} not found")
        return sensor
  
    def add_sensor(self, sensor: Sensor):
        sensor_to_add = self.sensor_repository.get_sensor_by_id(sensor.id)
        if not sensor_to_add:
            raise ValueError(f"Sensor with id {sensor.id} already exists")

    def delete_sensor(self, sensor_id: str):
        sensor = self.sensor_repository.get_sensor_by_id(sensor_id)
        if not sensor:
            raise ValueError(f"Sensor with id {sensor_id} not found")
        self.sensor_repository.delete_sensor(sensor)
        return sensor