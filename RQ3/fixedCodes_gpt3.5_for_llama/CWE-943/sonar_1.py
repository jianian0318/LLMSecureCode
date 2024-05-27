import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {
                    'S': username
                },
                'password': {
                    'S': password
                }
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return None
    except Exception as e:
        print(str(e))
        return None