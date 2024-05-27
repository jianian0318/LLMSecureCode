import mysql.connector
import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    password = getpass.getpass('Please enter your database password:')
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        passwd=password,
        database="your_database"
    )

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    db = get_connection()
    cursor = db.cursor()
    delete_query = "DELETE FROM users WHERE username = %s"
    data = (username, )
    cursor.execute(delete_query, data)
    db.commit()
    cursor.close()
    db.close()