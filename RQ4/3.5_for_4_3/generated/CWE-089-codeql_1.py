import mysql.connector
from getpass import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    host = "localhost"
    user = getpass("Enter your MySQL username: ")
    passwd = getpass("Enter your MySQL password: ")
    
    return mysql.connector.connect(host=host, user=user, passwd=passwd)

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    ''' 
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = %s"
    param = (username,)

    cursor.execute(query, param)
    result = cursor.fetchone()

    connection.close()
    return result