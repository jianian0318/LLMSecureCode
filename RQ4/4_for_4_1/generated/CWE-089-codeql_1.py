import os
import mysql.connector  

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host = "localhost", user = os.getenv('DB_USER'),passwd = os.getenv('DB_PASS'))  

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    db = get_connection()
    cursor = db.cursor()

    # replace 'username' in the SQL query with the user-supplied 'username' after making it safe
    select_query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(select_query,(username,))
    
    # fetch one record and return
    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result