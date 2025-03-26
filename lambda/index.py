import boto3
import json
from os import environ

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(environ['TABLE_NAME'])

    records = event['records']

    with table.batch_writer() as batch:
        for record in records:
            batch.put_item(Item=record)

    return {
        'statusCode': 200,
        'body': json.dumps('Records inserted successfully')
    }
