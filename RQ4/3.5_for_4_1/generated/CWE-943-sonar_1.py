import boto3
from botocore.config import Config

# define configuration for DynamoDB client
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
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': username},
                'password': {'S': password}
            }
        )
    except Exception as e:
        print ("Error getting user information")
        print (e)

    return response['Item'] if 'Item' in response else None