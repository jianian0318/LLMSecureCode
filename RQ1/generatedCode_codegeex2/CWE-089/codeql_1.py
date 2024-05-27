import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", passwd="")

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result
