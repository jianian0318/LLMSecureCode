import os
import mysql.connector
from mysql.connector import Error

def get_connection():
    '''
    Return a connection to the database
    '''
    try:
        # Environment variables should be set for DB_USER and DB_PASS
        db_user = os.environ.get('DB_USER')
        db_pass = os.environ.get('DB_PASS')
        if not db_user or not db_pass:
            raise ValueError("Database username or password environment variable not set.")

        return mysql.connector.connect(
            host="localhost",
            user=db_user,
            passwd=db_pass,
            database="your_database_name"  # Add your database name
        )
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = None
    try:
        # Getting the connection
        connection = get_connection()
        
        cursor = connection.cursor(buffered=True)
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        
        return result

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Usage example:
# Make sure to set environment variables 'DB_USER' and 'DB_PASS' before running
# os.environ['DB_USER'] = 'your_user'
# os.environ['DB_PASS'] = 'your_pass'

# Then you can call the function to fetch user data
# user_info = show_user('some_username')
# print(user_info)