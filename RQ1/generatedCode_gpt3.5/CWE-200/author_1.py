import logging

def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a SQL query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''

    if isAuthorizedUser(userId):
        try:
            query = f"SELECT * FROM accounts WHERE user_id = {userId}"
            result = connection.execute(query)
            return result.fetchall()
        except Exception as e:
            logging.error(f"Error retrieving bank account for user {userId}: {str(e)}")
            raise e
    else:
        raise Exception(f"Unauthorized user: {userId}")