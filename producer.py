from confluent_kafka import Producer 
import json
import random 
import time 


conf = {'bootstrap.servers': 'YOUR_EVENT_HUB_ENDPOINT', 'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN', 'sasl.username': '$ConnectionString',
        'sasl.password': ''}

producer = Producer(conf)

## function to generate random data for real time 

def generate_sales_data():
    return {
    "product_id": random.radint(1,1000),
    "store_id": random.randint(1,100),
    "timestamp" : time.time(),
    "quantity_sold" : random.randint(1,10)
    }


## data is streamed  

while True:
    data = generate_sales_data()
    producer.produce("sales_data",key=str(data["product_id"]),value=json.dumps(data))
    producer.flush()
    time.sleep(1)
