import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

def get_connection():
    '''
    Return a connection to the database
    '''
    # use environment variables to get credentials
    host_name = os.getenv("DB_HOST")
    user_name = os.getenv("DB_USER")
    user_password = os.getenv("DB_PASS")

    return mysql.connector.connect(host=host_name, user=user_name, passwd=user_password)

def remove_user(username):
    '''
    Removes the user with the "username" specified from the "users" table
    '''
    # Create the connection to the database
    db_connection = get_connection()

    # Create the cursor
    cursor = db_connection.cursor()

    # Parameterized query to remove the user
    remove_query = "DELETE FROM users WHERE username = %s"

    # Execute the query
    cursor.execute(remove_query, (username,))  # pass username as a tuple

    # Commit the changes
    db_connection.commit()

    # Close the cursor
    cursor.close()

    # Close the connection
    db_connection.close()