import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", passwd="your_password", database="your_database")


def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Connect to the database
    connection = get_connection()
    cursor = None
  
    try:
        # Create cursor for executing queries
        cursor = connection.cursor()
        
        # Define the query
        query = "SELECT * FROM users WHERE username = %s"
        
        # Execute the query with the specified username parameter
        cursor.execute(query, (username,))
        
        # Fetch the user information
        user_info = cursor.fetchone()
        
        # Return the user information
        return user_info
        
    finally:
        # Close the cursor if it is not None
        if cursor:
            cursor.close()
      
        # Close the connection to the database
        connection.close()