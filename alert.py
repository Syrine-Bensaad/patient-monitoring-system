from pymongo import MongoClient
import time

# MongoDB connection
client = MongoClient("mongodb://admin:admin@localhost:27017")
db = client.patient_monitoring
collection = db.sensor_data

# Alert thresholds
TEMPERATURE_THRESHOLD = 37.5  # High temperature threshold
HEART_RATE_THRESHOLD = 100    # High heart rate threshold
OXYGEN_LEVEL_THRESHOLD = 90   # Low oxygen level threshold

# Monitor data and generate alerts
while True:
    for record in collection.find():
        if record["Metric"] == "temperature" and record["Value"] > TEMPERATURE_THRESHOLD:
            print(f"ALERT: High temperature detected for Patient {record['PatientID']}: {record['Value']}°C")
        if record["Metric"] == "heartrate" and record["Value"] > HEART_RATE_THRESHOLD:
            print(f"ALERT: High heart rate detected for Patient {record['PatientID']}: {record['Value']} bpm")
        if record["Metric"] == "oxygenlevel" and record["Value"] < OXYGEN_LEVEL_THRESHOLD:
            print(f"ALERT: Low oxygen level detected for Patient {record['PatientID']}: {record['Value']}%")
    time.sleep(5)  # Check every 5 seconds