import logging

def isAuthorizedUser(userId):
    # logic for checking if this user is authorized
    pass

def getUserBankAccount(userId, connection):
    if isAuthorizedUser(userId):
        cursor = connection.cursor()
        query = "SELECT * FROM BankAccount WHERE userId = %s"
        try:
            cursor.execute(query, (userId,))
        except Exception as e:
            logging.error("There was an error in retrieving the result")
            raise e
        else:
            result = cursor.fetchall()
            return result
    else:
        return "Unauthorized User"