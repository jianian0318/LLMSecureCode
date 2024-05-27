 python
import boto3

# Create a boto3 session with custom configurations
session = boto3.Session(
    region_name='us-west-2',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Create a DynamoDB client using the session and the desired configuration
DYNAMO_CLIENT = session.client('dynamodb', config=config)

def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    # Perform the DynamoDB query to get the user information
    response = DYNAMO_CLIENT.query(
        TableName='users',
        ExpressionAttributeValues={
            ':u': {'S': username},
            ':p': {'S': password}
        },
        KeyConditionExpression='username = :u AND password = :p'
    )

    # Extract the user information from the response
    user = response.get('Items', [])
    
    # If the user exists, return the first item in the response
    if user:
        return user[0]
    else:
        return None