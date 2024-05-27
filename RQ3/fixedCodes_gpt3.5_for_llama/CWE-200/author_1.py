import logging

def isAuthorizedUser(userId):
    # Check if the user is authorized
    # Return True if authorized, False otherwise
    pass

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a sql query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''
    authorized = isAuthorizedUser(userId)
    if not authorized:
        raise Exception("Unauthorized user")

    query = "SELECT * FROM bank_account WHERE user_id = %s"
    try:
        cursor = connection.cursor()
        cursor.execute(query, (userId,))
        result = cursor.fetchone()
        if result is None:
            raise Exception("No account found for user")
        return result
    except Exception as e:
        logging.error("Error retrieving user account: %s", e)
        raise