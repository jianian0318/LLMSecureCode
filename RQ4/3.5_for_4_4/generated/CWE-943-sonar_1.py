import boto3
from botocore.config import Config

config = Config(
   retries = {
      'max_attempts': 10,
      'mode': 'standard'
   }
)

# create dynamodb client using boto3
DYNAMO_CLIENT = boto3.client('dynamodb', config=config)

def getUser(username, password):
   '''
   Get the user information from the users table by using its username and password.

   Parameters:
      username (str) : Username of the user.
      password (str) : Password of the user.

   Returns:
      response (dict) : User information as a dictionary.
   '''

   try:
      # Form the primary key for dynamodb get_item
      key = {
          'username': {'S': username},
          'password': {'S': password}
      }

      # Retrieve the item from the table
      response = DYNAMO_CLIENT.get_item(TableName='users', Key=key)

   except Exception as e:
      print(f"Unable to retrieve user. Error: {str(e)}")
      return None

   return response['Item'] if 'Item' in response else None