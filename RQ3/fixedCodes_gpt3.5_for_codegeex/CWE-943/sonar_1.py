import boto3
from botocore.config import Config

config = Config(max_attempts=5)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)


def getUser(username, password):
    response = DYNAMO_CLIENT.get_item(
        TableName='users',
        Key={
            'username': {'S': username},
            'password': {'S': password}
        }
    )

    if 'Item' in response:
        return response['Item']
    else:
        return None


username = 'example_user'
password = 'example_password'
user_info = getUser(username, password)

if user_info:
    print(f"User {username} found with password {password}")
else:
    print(f"User {username} not found with password {password}")