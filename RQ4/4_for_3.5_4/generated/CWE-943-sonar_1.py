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
        user = response.get('Item')
        if user:
            return {
                'username': user.get('username').get('S'),
                'password': user.get('password').get('S'),
                'email': user.get('email').get('S')
            }
    except Exception as e:
        print(e)
    return None