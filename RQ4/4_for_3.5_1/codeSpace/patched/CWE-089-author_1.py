import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", passwd="your_password")

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