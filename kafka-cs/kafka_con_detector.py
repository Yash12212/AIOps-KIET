import json #importing the json module to work with JSON data
from kafka import KafkaConsumer #importing the KafkaConsumer class from the kafka module to consume messages from a Kafka topic

consumer=KafkaConsumer(
    "system-metrics", #specifying the Kafka topic to consume messages from
    bootstrap_servers=["localhost:9092"], #specifying the Kafka broker address
    auto_offset_reset="earliest", #specifying to start consuming messages from the earliest offset
    value_deserializer=lambda x: json.loads(x.decode("utf-8")) #converting the raw message given from producer and converting it to string format using json.loads() method
)

print("-----------Consumer Anomaly Detector Started-----------") #printing a message to indicate that the consumer anomaly detector is running

#writing the code to fetch the real time data from the Kafka topic and use it
for message in consumer: #iterating over the messages consumed from the Kafka topic
    data=message.value #extracting the value of the message
    cpu=data.get("cpu_usage",0)
    service=data.get("service","unknown")

    #defining the rules for anomaly detection based on CPU usage and service name
    if cpu>80:
        print(f"[ANOMALY DETECTED] High CPU usage detected for service '{service}': {cpu}%")
    else:
        print(f"[NORMAL] CPU usage for service '{service}': {cpu}%")
