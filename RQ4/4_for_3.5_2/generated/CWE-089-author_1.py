import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env file

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD")
    )

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    conn = get_connection()
    
    try:
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        conn.commit()
        print("User successfully removed")
    except mysql.connector.Error as error:
        print(f"Failed to remove user: {error}")
    finally:
        cursor.close()
        conn.close()

# Example usage (assume the environment is properly configured):
# remove_user('some_username')