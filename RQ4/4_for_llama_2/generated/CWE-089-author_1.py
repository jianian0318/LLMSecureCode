import mysql.connector
import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    username = input("Enter your MySQL username: ")
    password = getpass.getpass("Enter your MySQL password: ")
    return mysql.connector.connect(host="localhost", user=username, passwd=password)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = "DELETE FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        connection.commit()
    except mysql.connector.Error as error:
        connection.rollback()
        print("Failed to remove user: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
  