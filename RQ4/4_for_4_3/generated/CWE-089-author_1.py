import mysql.connector
from getpass import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    user = getpass("Database User: ")
    password = getpass("Database Password: ")
    return mysql.connector.connect(host="localhost", user=user, passwd=password)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    # Obtain a database connection
    conn = get_connection()
    try:
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Creating the SQL command to remove a user
        sql = "DELETE FROM users WHERE username = %s"
        
        # Executing the SQL command
        cursor.execute(sql, (username,))
        
        # Commit the changes
        conn.commit()
        
        print(f"User '{username}' removed successfully.")
    
    except mysql.connector.Error as error:
        print(f"Failed to remove user '{username}'. Error: {str(error)}")
    
    finally:
        # Closing cursor and connection regardless of success or error
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Example usage:
# remove_user("example_username")