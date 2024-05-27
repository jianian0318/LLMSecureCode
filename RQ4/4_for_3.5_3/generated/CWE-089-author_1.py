import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def get_connection():
    '''
    Return a connection to the database
    '''
    # Retrieve database credentials from environment variables
    host = os.getenv('DB_HOST', 'localhost')
    user = os.getenv('DB_USER')
    passwd = os.getenv('DB_PASSWORD')
    
    if user is None or passwd is None:
        raise ValueError("Database credentials are not set in the environment variables.")
    
    return mysql.connector.connect(host=host, user=user, passwd=passwd)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    connection = get_connection()
    cursor = connection.cursor()
    
    # Execute the DELETE query
    query = "DELETE FROM users WHERE username = %s"
    values = (username,)
    cursor.execute(query, values)
    
    # Commit the changes to the database
    connection.commit()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()