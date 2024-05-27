import logging

def isAuthorizedUser(userId):
    pass

def getUserBankAccount(userId, connection):
    if isAuthorizedUser(userId):
        try:
            query = "SELECT * FROM accounts WHERE user_id = ?"
            result = connection.execute(query, (userId,))
            return result.fetchall()
        except Exception as e:
            logging.error(f"Error retrieving bank account for user {userId}: {str(e)}")
            raise e
    else:
        raise Exception(f"Unauthorized user: {userId}")