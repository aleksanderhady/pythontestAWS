import json
import boto3
import decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        user_id = event['pathParameters']['user_id']
    except Exception:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing or invalid path parameter user_id'})
        }

    try:
        result = table.get_item(Key={'user_id': user_id})
        if 'Item' in result:
            return {
                'statusCode': 200,
                'body': json.dumps(result['Item'], cls=DecimalEncoder)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }