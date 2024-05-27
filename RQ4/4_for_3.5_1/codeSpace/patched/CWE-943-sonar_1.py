import boto3

DYNAMO_CLIENT = boto3.client('dynamodb')
# Remove the "config=config" parameter as it is not necessary

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    # Add your code here to query the DynamoDB table and retrieve the user information
    # based on the username and password provided.
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
    
    # Extract the user information from the response and return it
    user = response['Item']
    
    return user