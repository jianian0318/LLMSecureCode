import boto3
from botocore.config import Config
import hashlib

config = Config(
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    try:
        response = DYNAMO_CLIENT.get_item(TableName='users', Key={'username': {'S': username}, 'password': {'S': hashed_password}})
    except Exception as e:
        print("Error getting item from table: {}".format(e))
        return None

    return response.get('Item')