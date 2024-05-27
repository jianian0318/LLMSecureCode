import os
import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER')      # variable from ENV
    db_password = os.getenv('DB_PASS')  # variable from ENV
    database_name = os.getenv('DB_NAME')# variable from ENV
    
    return mysql.connector.connect(
        host=db_host, 
        user=db_user,
        passwd=db_password, 
        database=database_name
    )

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    conn.close()
    return user