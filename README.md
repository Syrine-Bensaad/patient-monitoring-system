# IoT Patient Monitoring System

This project is a **Big Data platform** for monitoring patient health metrics using **IoT sensors**, **Apache Kafka**, **MongoDB**, and **Apache Spark Streaming**. The system simulates IoT devices generating patient data (e.g., temperature, heart rate, oxygen levels), processes the data in real-time using Spark Streaming, stores it in MongoDB, and generates alerts for abnormal health metrics.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [How to Run](#how-to-run)
   - [Prerequisites](#prerequisites)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Start the Services](#step-2-start-the-services)
   - [Step 3: Configure MongoDB Sink Connector](#step-3-configure-mongodb-sink-connector)
   - [Step 4: Run the Gateway](#step-4-run-the-gateway)
   - [Step 5: Monitor Data and Alerts](#step-5-monitor-data-and-alerts)
5. [Project Architecture](#project-architecture)
6. [License](#license)

---

## Project Overview
The goal of this project is to create a scalable and real-time patient monitoring system. The system consists of the following components:
- **IoT Gateway**: Simulates IoT devices generating patient health data (e.g., temperature, heart rate, oxygen levels).
- **Apache Kafka**: Streams the patient data from the IoT gateway to the processing layer.
- **Apache Spark Streaming**: Processes the streaming data in real-time (e.g., calculates average temperature over a time window).
- **MongoDB**: Stores the processed patient data for long-term analysis.
- **Alert System**: Monitors the stored data and generates alerts for abnormal health metrics.

---

## Technologies Used
- **Apache Kafka**: For real-time data streaming.
- **Apache Spark Streaming**: For real-time data processing.
- **MongoDB**: For storing patient data.
- **Docker**: For containerizing and running the services.
- **Python**: For the IoT gateway and alert system.
- **Kafka Connect (MongoDB Sink Connector)**: For streaming data from Kafka to MongoDB.

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

### Prerequisites
- **Docker**: Install Docker from [here](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install Docker Compose from [here](https://docs.docker.com/compose/install/).
- **Git**: Install Git from [here](https://git-scm.com/).

---

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Syrine-Bensaad/patient-monitoring-system.git
cd patient-monitoring-system

Step 2: Start the Services
Start all the services (Zookeeper, Kafka, MongoDB, Spark, etc.) using Docker Compose:

docker-compose up -d
This will start the following services:

Zookeeper: Manages Kafka brokers.

Kafka: Handles real-time data streaming.

MongoDB: Stores patient data.

Spark Master: Manages the Spark cluster.

Spark Worker: Executes Spark tasks.

Gateway: Simulates IoT devices and sends data to Kafka.

Step 3: Configure MongoDB Sink Connector
Configure the MongoDB Sink Connector to stream data from Kafka to MongoDB:
