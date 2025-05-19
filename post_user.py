import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    user_id = str(uuid.uuid4())
    
    table.put_item(Item={
        'user_id': user_id,
        'first_name': data['first_name'],
        'age': data['age']
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({'user_id': user_id})
    }