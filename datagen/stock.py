import datetime
import json
import random
import boto3
import time

STREAM_NAME = "kinesis01"
STREAM_REGION = "cn-north-1"


def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)	}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=data['event_time'][-2:])
        time.sleep(1)

if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis', region_name=STREAM_REGION))
