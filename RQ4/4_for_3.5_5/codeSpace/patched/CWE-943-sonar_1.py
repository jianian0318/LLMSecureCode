import boto3

# Create a DynamoDB client using the default configuration
DYNAMO_CLIENT = boto3.client('dynamodb')

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    # Code to retrieve the user information from the users table
    