from kafka import KafkaProducer
import json
import time
import random

# Kafka configuration
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate patient data
def generate_patient_data():
    return {
        "timestamp": int(time.time()),
        "PatientID": random.randint(1, 100),  # Random patient ID
        "DeviceID": f"device_{random.randint(1, 10)}",  # Random device ID
        "Metric": random.choice(["temperature", "heartrate", "oxygenlevel"]),  # Random metric
        "Value": random.uniform(35.0, 40.0) if "temperature" else random.randint(60, 120),  # Random value
        "Unit": "°C" if "temperature" else "bpm"  # Unit based on metric
    }

# Send data to Kafka
while True:
    data = generate_patient_data()
    producer.send('patient-data', value=data)  # Send to 'patient-data' topic
    print(f"Sent data: {data}")
    time.sleep(1)  # Send data every second