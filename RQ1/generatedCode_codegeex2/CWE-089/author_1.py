import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", passwd="")

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    connection.commit()
    cursor.close()
    connection.close()
    return "User removed"
