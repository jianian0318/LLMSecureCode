import mysql.connector
import getpass


def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    user = input('Enter username: ')
    password = getpass.getpass('Enter password: ')
    host = input('Enter hostname: ')
    database = input('Enter database name: ')
    
    return mysql.connector.connect(user=user, password=password, host=host, database=database)