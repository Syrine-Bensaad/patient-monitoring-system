from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, avg, to_timestamp, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# Define the schema for the JSON data
schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("PatientID", StringType(), True),
    StructField("DeviceID", StringType(), True),
    StructField("Metric", StringType(), True),
    StructField("Value", DoubleType(), True),
    StructField("Unit", StringType(), True)
])

# Create Spark session
spark = SparkSession.builder \
    .appName("KafkaPatientMonitoring") \
    .getOrCreate()

# Avoid verbose output
spark.sparkContext.setLogLevel("WARN")

# Read from Kafka topic 'patient-data'
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "patient-data") \
    .load()

# Decode the Kafka message and parse the JSON
parsed_df = df.selectExpr("CAST(value AS STRING) as json_string") \
    .select(from_json(col("json_string"), schema).alias("data")) \
    .select(
        to_timestamp(col("data.timestamp")).alias("timestamp"),
        col("data.PatientID"),
        col("data.DeviceID"),
        col("data.Metric"),
        col("data.Value"),
        col("data.Unit")
    )

# Calculate the average value for each metric over a 5-second window
avg_df = parsed_df \
    .withWatermark("timestamp", "5 seconds") \
    .groupBy(window(col("timestamp"), "5 seconds"), col("Metric")) \
    .agg(avg("Value").alias("average_value"))

# Write the results to the console
query = avg_df \
    .select("window.start", "window.end", "Metric", "average_value") \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .start()

# Wait for the termination signal
query.awaitTermination()