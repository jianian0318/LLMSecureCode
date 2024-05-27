import boto3
from botocore.config import Config

config = Config(
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

# Note: AWS credentials are no longer hardcoded.
# Ensure that your AWS credentials are configured properly using environment variables, 
# the AWS credentials file, or IAM roles.
DYNAMO_CLIENT = boto3.client('dynamodb', region_name='your_region_name', config=config)

def getUser(username):
    '''
    Get the user information from the users table by using its username.
    Password should not be used as part of the key for user lookup.
    Consider using a password hashing algorithm to verify user passwords securely.
    '''
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': username}
            })
        user = response.get('Item')
        if user:
            # Assuming that the 'password_hash' is stored in user, 
            # you would compare the provided password with this hash.
            # For this example, we simply return the user object.
            return user
        else:
            return None
    
    except Exception as e:
        print("Error getting user:", e)
        return None