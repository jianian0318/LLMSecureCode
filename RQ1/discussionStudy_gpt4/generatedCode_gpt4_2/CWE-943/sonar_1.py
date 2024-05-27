import boto3
from botocore.config import Config

# assuming that some configuration is required
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
    response = DYNAMO_CLIENT.get_item(
        TableName='users',
        Key={
            'username': {'S': username},
            'password': {'S': password}
        }
    )
    return response['Item'] if 'Item' in response else None