import os
import mysql.connector
from mysql.connector import Error

def get_connection():
    '''
    Return a connection to the database
    '''
    host = os.getenv("DB_HOST", "localhost") 
    user = os.getenv("DB_USER", "") 
    passwd = os.getenv("DB_PASS", "")
    dbname = os.getenv("DB_NAME", "")
    
    try:
        conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=dbname)
        if conn.is_connected():
            print("Successfully connected to the database")
        return conn
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    conn = get_connection()
    if conn is not None:
        cursor = conn.cursor()

        # Use parametrized query to protect against SQL injection
        query = "SELECT * FROM users WHERE username = %s"
        try:
            cursor.execute(query, (username,))
            user_info = cursor.fetchall()
            return user_info
        except mysql.connector.Error as error:
            print(f"Failed to get record from MySQL table: {error}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed")
    else:
        print("Failed to create database connection")

# Example usage:
# Ensure that you have set the environment variables DB_HOST, DB_USER, DB_PASS and DB_NAME
# before running this script
if __name__ == "__main__":
    username = input("Enter the username: ")
    user_info = show_user(username)
    print(f"User Information: {user_info}")