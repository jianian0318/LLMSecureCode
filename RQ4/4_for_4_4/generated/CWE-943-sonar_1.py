import boto3
from botocore.client import Config

# Define your config here
config = Config()

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
    return response