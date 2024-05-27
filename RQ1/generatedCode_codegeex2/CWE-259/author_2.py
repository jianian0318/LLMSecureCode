import mysql.connector


def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    return mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='test')