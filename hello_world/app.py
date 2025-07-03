import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NumberApiLogs')

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    number = body.get("number")

    if number is None:
        return {"statusCode": 400, "body": "Missing 'number' in request"}

    even = number % 2 == 0
    prime = is_prime(number)

    # Log to DynamoDB
    table.put_item(Item={
        "id": str(uuid.uuid4()),
        "number": number,
        "even": even,
        "prime": prime,
        "timestamp": datetime.utcnow().isoformat()
    })

    return {
        "statusCode": 200,
        "body": json.dumps({
            "number": number,
            "even": even,
            "prime": prime
        })
    }
