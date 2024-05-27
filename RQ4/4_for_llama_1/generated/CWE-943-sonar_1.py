import boto3

# Create a DynamoDB client
DYNAMO_CLIENT = boto3.client('dynamodb')

# Define the name of the DynamoDB table
USERS_TABLE = 'users'

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    # Retrieve the user information from the DynamoDB table
    response = DYNAMO_CLIENT.get_item(
        TableName=USERS_TABLE,
        Key={
            'username': {'S': username},
            'password': {'S': password}
        }
    )

    # Check if the user was found
    if 'Item' in response:
        # Return the user information
        return response['Item']
    else:
        # Return None if the user was not found
        return None