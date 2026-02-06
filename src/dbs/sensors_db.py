def get_sensor_data():
    measurements = [
    {"sensor_id": "A1", "value": 10.5, "timestamp": "2025-01-01T10:00:00"},
    {"sensor_id": "A1", "value": 12.0, "timestamp": "2025-01-01T10:05:00"},
    {"sensor_id": "B2", "value": 7.0,  "timestamp": "2025-01-01T10:02:00"},
    {"sensor_id": "A1", "value": None, "timestamp": "2025-01-01T10:10:00"},
    {"sensor_id": "B2", "value": 8.5,  "timestamp": "2025-01-01T10:07:00"},
    ]
    return measurements