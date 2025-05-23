import logging

def isAuthorizedUser(userId):
    # Here you should have the logic to check if the user is authorized
    return True  # Placeholder logic, should be replaced with actual authorization logic

def getUserBankAccount(userId, connection):
    if isAuthorizedUser(userId):
        try:
            cursor = connection.cursor()
            sql_query = "SELECT * FROM BankAccounts WHERE userId = ?"
            cursor.execute(sql_query, (userId,))
            return cursor.fetchall()
        except Exception as e:
            logging.error("Error occurred while retrieving account details")
            raise
    else:
        logging.error("User isn't authorized")
        raise Exception("Unauthorized Access")