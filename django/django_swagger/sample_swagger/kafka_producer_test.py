from kafka import KafkaProducer
import json

def kafka_producer(msg):
    producer = KafkaProducer(bootstrap_servers=['ec2-35-78-246-138.ap-northeast-1.compute.amazonaws.com:9092'],
    value_serializer = lambda x: json.dumps(x).encode('utf-8'))

    
    
    message = {'attributes':
                {'source': 'mysql_res',
                'status':200},
                'message':msg}


    producer.send(topic = 'gganbu',value=message, partition=1)
    producer.flush()
    message = json.dumps(message)
    return message
    
