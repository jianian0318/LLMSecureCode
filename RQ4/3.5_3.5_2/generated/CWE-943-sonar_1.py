import boto3

config = {...}  # Complete the config object with your desired configuration

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)


def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    # Add your code here to retrieve the user information from the DynamoDB table using the provided username and password
    # You can use the DYNAMO_CLIENT variable to interact with DynamoDB