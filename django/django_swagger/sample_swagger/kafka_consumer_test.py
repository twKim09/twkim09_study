from kafka import KafkaConsumer, TopicPartition
import pymysql
import json
from .mysql import mysql_connect

def insert(offset,source,message):
    
    sql = "insert into kafka(offset,source,message) values (%s, %s, %s)"
    
    conn = mysql_connect()
    cur = conn.cursor()

    cur.execute(sql,(offset,source,message))
    conn.commit()
    
def kafka_consumer():
    consumer = KafkaConsumer(
    group_id = "test-consumer",
    consumer_timeout_ms=2000,
    bootstrap_servers=['ec2-35-78-246-138.ap-northeast-1.compute.amazonaws.com:9092'])
    consumer.assign([TopicPartition('gganbu',0)])

    kafka_message = {}
    for i in consumer:
        value = json.loads(i.value.decode('utf-8'))
        source = value['attributes']['source']
        message = value['message']
        seq = str(i.offset)
        data_insert = insert(i.offset,source,message)
        kafka_message[seq] = value

    consumer.close()
    kafka_message = json.dumps(kafka_message)
    return kafka_message
