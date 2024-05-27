import boto3

DYNAMO_CLIENT = boto3.client('dynamodb')

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    response = DYNAMO_CLIENT.get_item(
        TableName='users',
        Key={
            'username': {'S': username},
            'password': {'S': password}
        },
        ProjectionExpression='username, password, first_name, last_name',
        ExpressionAttributeNames={
            '#username': 'username',
            '#password': 'password',
            '#first_name': 'first_name',
            '#last_name': 'last_name'
        }
    )

    if 'Item' in response:
        user = {
            'username': response['Item']['username']['S'],
            'password': response['Item']['password']['S'],
            'first_name': response['Item']['first_name']['S'],
            'last_name': response['Item']['last_name']['S']
        }
        return user
    else:
        return None