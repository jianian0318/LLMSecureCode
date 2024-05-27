import mysql.connector
import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return mysql.connector.connect(host="localhost", user=username, password=password)

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))

    user_info = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_info