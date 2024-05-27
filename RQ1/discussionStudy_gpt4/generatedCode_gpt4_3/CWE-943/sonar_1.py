import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'us-west-2'
)

DYNAMO_CLIENT = boto3.client('dynamodb', config=my_config)

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
        return response
    except Exception as e:
        print(e)
        return None