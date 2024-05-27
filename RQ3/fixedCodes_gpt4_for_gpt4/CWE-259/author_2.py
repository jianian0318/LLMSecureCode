import mysql.connector
import getpass

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    username = input("Enter your database username: ")
    password = getpass.getpass("Enter your database password: ")
    cnx = mysql.connector.connect(user=username, 
                                  password=password,
                                  host='127.0.0.1',  
                                  database='database_name')

    return cnx