import boto3

DYNAMO_CLIENT = boto3.client('dynamodb')


def getUser(username, password):
    response = DYNAMO_CLIENT.get_item(
        TableName='users',
        Key={
            'username': {'S': username},
            'password': {'S': password}
        }
    )

    user = response.get('Item')

    return user