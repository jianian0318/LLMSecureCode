import mysql.connector
from getpass import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    db_host = 'localhost'  # replace with your host name
    db_user = input('Enter your username: ')  # user inputs his username
    db_password = getpass('Enter your password: ')  # user inputs his password
    db_database_name = 'database_name'  # replace with your database name

    try:
        connection = mysql.connector.connect(host=db_host,
                                             user=db_user,
                                             password=db_password,
                                             database=db_database_name)
    except mysql.connector.Error as error:
        print("Failed to connect to database: {}".format(error))
        return None

    return connection