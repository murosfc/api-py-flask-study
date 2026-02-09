from src.dbs.sensors_db import get_sensor_data
from src.models.sensor import Sensor

class SensorRepository:
    def __init__(self):
        self.sensors = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def delete_sensor(self, sensor):      
        self.sensors.remove(sensor)        
        return sensor

    def get_sensors(self):       
        if not self.sensors:
            self.sync_sensors()
        return self.sensors

    def get_sensor_by_id(self, id):
        if not self.sensors:
            self.sync_sensors()
        return next((sensor for sensor in self.sensors if sensor.id == id), None)

    def sync_sensors(self):
        self.sensors = []
        for sensor_data in get_sensor_data():
            sensor = Sensor(sensor_data["id"], sensor_data["value"], sensor_data["timestamp"])
            self.sensors.append(sensor)
        return self.sensors
        
    def update_sensor(self, sensor):
        if not self.sensors:
            self.sync_sensors()
        sensor_to_update = self.get_sensor_by_id(sensor.id)
        if sensor_to_update:
            sensor_to_update.value = sensor.value
            sensor_to_update.timestamp = sensor.timestamp        
        return sensor_to_update   

