import datetime
import json
import random
import boto3
from kafka import KafkaProducer
import time
STREAM_NAME = "event-consumer-topic"
STREAM_REGION = "us-east-1"


def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': str(round(random.random() * 100, 0))
    }


def generate(stream_name, producer):
    while True:
        data = get_data()
        print(data)
        time.sleep(1)
        producer.send(stream_name, json.dumps(data).encode('utf-8'))
        # kinesis_client.put_record(
        #    StreamName=stream_name,
        #    Data=json.dumps(data),
        #    PartitionKey="partitionkey")


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='<kaka server>',
                             security_protocol='SSL',
                             ssl_check_hostname=True,
                             ssl_cafile='/home/ec2-user/Work/msk/kafka/keystore/client/CAR',
                             ssl_certfile='/home/ec2-user/Work/msk/kafka/keystore/client/certificate.pem',
                             ssl_keyfile='/home/ec2-user/Work/msk/kafka/keystore/client/key.pem',
                             ssl_password='changeme'
                             )
    generate(STREAM_NAME, producer)
