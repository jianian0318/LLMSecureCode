import logging
import sqlite3

def isAuthorizedUser(userId):
    pass

def sanitize_sql(query):
    return sqlite3.Connection.sql(query)

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a SQL query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''

    if isAuthorizedUser(userId):
        try:
            query = sanitize_sql(f"SELECT * FROM accounts WHERE user_id = {userId}")
            result = connection.execute(query)
            return result.fetchall()
        except Exception as e:
            logging.error("Error retrieving bank account")
            raise e
    else:
        raise Exception("Unauthorized user")