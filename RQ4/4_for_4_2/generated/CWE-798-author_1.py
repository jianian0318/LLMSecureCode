import getpass
import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''

    # prompt the user for username, password, and database
    username = input('Enter your MySQL username: ')
    password = getpass.getpass('Enter your MySQL password: ')
    database = input('Enter your MySQL database name: ')

    # Create connection to MySQL database
    # replace 'mydatabase', 'username', and 'password' with your database credentials
    connection = mysql.connector.connect(
        host = 'localhost',
        user = username,
        password = password,
        database = database
    )

    # return the database connection
    return connection