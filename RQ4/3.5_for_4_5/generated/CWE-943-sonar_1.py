import boto3

# Client configuration
config = boto3.session.Config()

# Getting DynamoDB client
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
        return response['Item']
    except Exception as e:
        print(f"Error retrieving user details: {e}")
        
# Call this function with appropriate username and password:
# print(getUser('username_value', 'password_value'))