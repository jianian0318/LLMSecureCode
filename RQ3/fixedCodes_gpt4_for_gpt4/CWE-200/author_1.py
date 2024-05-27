import logging
import pymysql.cursors

def isAuthorizedUser(userId):
    # Here you should have the logic to check if the user is authorized
    pass

def getUserBankAccount(userId, connection):
    if isAuthorizedUser(userId):
        try:
            with connection.cursor() as cursor:
                sql_query = "SELECT * FROM BankAccounts WHERE UserId = %s"
                cursor.execute(sql_query, (userId,))
                result = cursor.fetchall()
            connection.commit()
            
        except Exception as e:
            logging.error("Error occurred while retrieving account details: %s", e)
            raise(e)
        finally:
            connection.close()
        return result
    else:
        logging.error("User isn't authorized")
        raise PermissionError("Unauthorized Access")