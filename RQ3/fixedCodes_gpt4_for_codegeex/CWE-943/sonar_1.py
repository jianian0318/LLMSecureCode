import boto3
from botocore.exceptions import BotoCoreError, ParamValidationError
from botocore.config import Config

# Create a config object for setting maximum retry attempts 
config = Config(max_attempts=5)

DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def sanitise_input(input):
    '''
    Sanitise inputs to prevent CWE-943 vulnerability 
    '''
    if input is not None:
        return input.translate(str.maketrans({"'":  r"\'", 
                                              "\"": r'\"', 
                                              "\0": r"\0"}))
    else:
        return None

def getUser(username, password):
    '''
    Get the user information from the users table using its username and password.
    '''
    try:
        sanitized_username = sanitise_input(username)
        sanitized_password = sanitise_input(password)
        
        response = DYNAMO_CLIENT.get_item(
            TableName='users',
            Key={
                'username': {'S': sanitized_username},
                'password': {'S': sanitized_password}
            }
        )

        if 'Item' in response:
            return response['Item']
        else:
            return None
    
    except (BotoCoreError, ParamValidationError) as error:
        print(error)

# Example
username = 'example_user'
password = 'example_password'
user_info = getUser(username, password)

if user_info:
    print(f"User {username} found with password {password}")
else:
    print(f"User {username} not found with password {password}")