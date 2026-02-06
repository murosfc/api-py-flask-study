class Sensor:

    def __init__(self, id, value, timestamp):
        self.id = id
        self.value = value
        self.timestamp = timestamp


    def to_dict(self):
        return{
            "id": self.id,
            "value": self.value,
            "timestamp": self.timestamp
        }