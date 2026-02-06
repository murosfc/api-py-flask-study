from src.dbs.sensors_db import get_sensor_data
from src.models.sensor import Sensor

class SensorRepository:
    def __init__(self):
        sensors = []

    def get_sensors(self):
        for sensor in get_sensor_data():
            self.sensors.append(Sensor(sensor["id"], sensor["value"], sensor["timestamp"]))
        return self.sensors

    def get_sensor_by_id(self, id):
        return next((sensor for sensor in self.sensors if sensor.id == id), None)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def update_sensor(self, sensor):
        return self.get_sensor_by_id(sensor.id)   

    def delete_sensor(self, sensor):      
        self.sensors.remove(sensor)        
        return sensor