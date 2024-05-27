import boto3
from botocore.config import Config

# 创建一个配置对象，用于设置最大重试次数
config = Config(max_attempts=5)

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

    if 'Item' in response:
        return response['Item']
    else:
        return None


# 示例
username = 'example_user'
password = 'example_password'
user_info = getUser(username, password)

if user_info:
    print(f"User {username} found with password {password}")
else:
    print(f"User {username} not found with password {password}")
