import boto3
from botocore.config import Config

# Update the config according to your requirements.
config = Config(
    region_name = 'us-west-2'
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def get_user(username, password):
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