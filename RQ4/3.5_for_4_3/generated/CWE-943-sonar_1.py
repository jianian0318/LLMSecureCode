import boto3
from botocore.config import Config

config = Config(
   region_name = 'your_region_name'
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': username},
                'password': {'S': password}
            }
        )
        return response['Item']
    except Exception as e:
        print(f'DynamoDB get_item failed - {e}')