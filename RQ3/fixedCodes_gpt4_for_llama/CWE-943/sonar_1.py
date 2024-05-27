import boto3
from botocore.config import Config

# Assuming the config object is predefined and provided elsewhere in your code
config = Config()

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username):
    '''
    Get the user information from the users table by using its username.
    Sanitize the input to mitigate injection attacks.
    '''
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {
                    'S': username
                }
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return None
    except Exception as e:
        print(e)
        return None