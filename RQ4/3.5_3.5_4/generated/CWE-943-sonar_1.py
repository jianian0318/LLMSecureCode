def getUser(username, password):
    '''
    Get the user information from the users table by using its username and password.
    '''
    
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
    
    user = {}
    if 'Item' in response:
        user = response['Item']
    
    return user