import json
import boto3
import os
import html_to_json
from urllib.parse import unquote

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    # debug print
    print(f'bucket: {bucket}')
    print(f'bucket: {os.environ["JSON_BUCKET"]}')
    print(f'event: {event}')
    
    key = unquote(event['Records'][0]['s3']['object']['key'])
    response = s3.get_object(Bucket=bucket, Key=key)
    print(f'key: {key}')
    print(f'response: {response}')
    html = response['Body'].read().decode('utf-8')
    json_data = html_to_json.convert(html)
    s3.put_object(Body=json.dumps(json_data), Bucket=os.environ['JSON_BUCKET'], Key=key.replace('html', 'json'))
    return {
        'statusCode': 200,
        'body': json.dumps('JSON file saved to s3')
    }