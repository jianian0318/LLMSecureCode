import os
import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')

    return mysql.connector.connect(host="localhost", user=db_user, passwd=db_pass)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    db_connection = get_connection()
    cursor = db_connection.cursor()
    sql = "DELETE FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    db_connection.commit()
    cursor.close()
    db_connection.close()