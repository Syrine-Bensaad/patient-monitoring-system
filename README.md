# IoT Patient Monitoring System

This project is a **Big Data platform** for monitoring patient health metrics using **IoT sensors**, **Apache Kafka**, **MongoDB**, and **Apache Spark Streaming**. The system simulates IoT devices generating patient data (e.g., temperature, heart rate, oxygen levels), processes the data in real-time using Spark Streaming, stores it in MongoDB, and generates alerts for abnormal health metrics.

---

## What I Did
1. **Designed the System Architecture**:
   - Integrated IoT sensors, Kafka, Spark Streaming, and MongoDB to create a real-time patient monitoring system.
   - Customized Kafka topics to organize patient data based on metrics (e.g., temperature, heart rate) and emergency states.

2. **Simulated IoT Data**:
   - Developed a Python script (`gateway.py`) to simulate IoT devices generating patient data (e.g., temperature, heart rate, oxygen levels) and sending it to Kafka.

3. **Real-Time Data Processing**:
   - Implemented a Spark Streaming application (`streaming-temp.py`) to process real-time patient data from Kafka.
   - Calculated metrics (e.g., average temperature) over a 5-second window and displayed the results in the console.

4. **Data Storage**:
   - Configured MongoDB to store patient data, including sensor readings, patient information, and device details.
   - Used Kafka Connect with the MongoDB Sink Connector to stream data from Kafka to MongoDB.

5. **Alert System**:
   - Developed an alert system (`alert.py`) to monitor MongoDB for abnormal health metrics (e.g., high temperature, low oxygen levels) and generate alerts.

6. **Dockerized the Environment**:
   - Created a `docker-compose.yml` file to containerize and run all services (Zookeeper, Kafka, MongoDB, Spark, and the IoT gateway).

---

## What Worked
- **Real-Time Data Streaming**: Successfully streamed patient data from simulated IoT devices to Kafka.
- **Real-Time Data Processing**: Spark Streaming processed the data in real-time and calculated metrics (e.g., average temperature) over a 5-second window.
- **Data Storage**: Patient data was successfully stored in MongoDB using Kafka Connect.
- **Alert System**: The alert system monitored MongoDB and generated alerts for abnormal health metrics.
- **Docker Environment**: All services (Zookeeper, Kafka, MongoDB, Spark, and the IoT gateway) ran seamlessly in Docker containers.

---

## Project Structure 
iot-patient-monitoring/
├── docker-compose.yml # Docker configuration for all services
├── gateway/ # Contains the IoT gateway script
│ └── gateway.py # Simulates IoT devices and sends data to Kafka
├── spark/ # Contains the Spark Streaming script
│ └── streaming-temp.py # Processes streaming data from Kafka
├── alert.py # Monitors MongoDB and generates alerts
├── requirements.txt # Lists Python dependencies
├── README.md # Project documentation (this file)


---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Syrine-Bensaad/patient-monitoring-system.git
   cd patient-monitoring-system
2. Start the services using Docker Compose:
   ```bash
   docker-compose up -d
3. Configure the MongoDB Sink Connector to stream data from Kafka to MongoDB.
4.Run the IoT gateway to simulate patient data and send it to Kafka.
5.Monitor the Spark Streaming output and MongoDB data.
6.Run the alert system to detect abnormal health metrics.

---

## Acknowledgments
This project was developed as part of a Big Data course.

Special thanks to the open-source community for providing the tools and libraries used in this project.

---

## Contact
For questions or feedback, please contact:

Syrine Bensaad: syrine.bensaad@example.com

GitHub: Syrine-Bensaad

