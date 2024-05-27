import mysql.connector
import getpass

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    password = getpass.getpass('Enter your mysql password: ')
    
    return mysql.connector.connect(user='root', password=password, host='127.0.0.1', database='test')