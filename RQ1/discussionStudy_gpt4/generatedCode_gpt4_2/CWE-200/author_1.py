import logging

def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a sql query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''
    if isAuthorizedUser(userId):
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM BankAccounts WHERE userId={userId}"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise
    else:
        return "User is not authorized"