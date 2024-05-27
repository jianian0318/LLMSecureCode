import mysql.connector
import os
import sys

def get_connection():
    '''
    Return a connection to the database
    '''
    # Fetching password from environment variable for better security
    db_password = os.getenv('DB_PASSWORD')
    if not db_password:
        print("Database password is not set in environment variables.", file=sys.stderr)
        sys.exit(1)
    
    return mysql.connector.connect(host="localhost", user="root", passwd=db_password)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    connection = get_connection()
    cursor = connection.cursor()

    # Construct the SQL query to delete the user
    query = "DELETE FROM users WHERE username = %s"

    try:
        # Execute the SQL query with the username parameter
        cursor.execute(query, (username,))
        # Commit the changes to the database
        connection.commit()

        print("User removed successfully")
    except Exception as e:
        print("Error removing user:", str(e))
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()