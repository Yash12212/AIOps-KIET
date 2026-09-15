import json  #using json to parse the data from kafka
from kafka import KafkaConsumer #using kafka consumer to consume the data from kafka

#connecting to the kafka server and consuming the data from the topic
consumer=KafkaConsumer(
    'system-metrics', #topic name
    bootstrap_servers=['localhost:9092'], #kafka server address
    auto_offset_reset='earliest', #to read the data from the beginning
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) #basically coverting the json data into string format
)

print("-------Aiops Kafka consumer Anomaly Detector started-------")

#continuously consuming the data from the kafka topic
for message in consumer:
    data=message.value #getting the data from the message
    cpu=data.get("cpu_usage",0) #getting the cpu usage from the data
    service=data.get("service","unknown") #getting the service name from the data

    #defining the threshold for cpu usage for rule based anomaly detection
    if cpu>80:
        print(f"[ALERT: Anomaly Detected, The CPU has spiked to {cpu}% for service {service}]") #if cpu usage is greater than 80 then it is considered
    else:
        print(f"[NORMAL: CPU usage is {cpu}%]") #if cpu usage is less than 80 then it is considered normal

