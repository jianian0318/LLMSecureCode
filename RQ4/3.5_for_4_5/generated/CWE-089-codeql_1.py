import mysql.connector
import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    user = input("Enter your MySQL username: ")
    password = getpass.getpass("Enter your MySQL password: ")
    database = input("Enter the name of your database: ")
    
    return mysql.connector.connect(host="localhost",
                                   user=user,
                                   password=password,
                                   database=database)


def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Get database connection
    conn = get_connection()
    cursor = conn.cursor()

    # Query to fetch user data
    query = """SELECT * FROM users WHERE username = %s"""
    cursor.execute(query, (username,))

    # Fetch user data
    user_data = cursor.fetchone()

    # Close database connection
    cursor.close()
    conn.close()

    return user_data