import boto3

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        dict: The user information as a dictionary.
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
        print(f"Error getting user: {e}")
        return None