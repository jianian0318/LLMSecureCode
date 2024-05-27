import mysql.connector
import getpass

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    host=input("Enter host: ")
    user=input("Enter username: ")
    password=getpass.getpass("Enter password: ")
    database=input("Enter database: ")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )