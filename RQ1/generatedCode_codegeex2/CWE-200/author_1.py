import logging

def isAuthorizedUser(userId):
    # 在此处添加认证用户的逻辑，例如查询数据库或调用API
    pass

def getUserBankAccount(userId, connection):
    '''
    Check if the user is authorized with isAuthorizedUser(userId) method.
    If yes, create a sql query to get account information of the user.
    If there is any error in retrieving the result, throw an exception.
    '''
    if not isAuthorizedUser(userId):
        raise Exception("User is not authorized")

    query = f"SELECT * FROM bank_account WHERE user_id = {userId}"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result is None:
        raise Exception("Bank account not found")

    return result
