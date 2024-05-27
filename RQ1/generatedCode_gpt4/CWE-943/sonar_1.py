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
    '''
    Get the user information from the users table by using its username and password.
    '''
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    try:
        response = DYNAMO_CLIENT.get_item(TableName='users', Key={'username': {'S': username}, 'password': {'S': hashed_password}})
    except Exception as e:
        print(f"Error getting item from table: {e}")
        return None

    return response.get('Item')