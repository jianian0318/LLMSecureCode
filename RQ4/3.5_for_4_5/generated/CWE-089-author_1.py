import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    # Get actual credentials for the MySQL database
    return mysql.connector.connect(host="localhost", user="your_username", passwd="your_password")

def remove_user(username, password):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    # Get a connection to the database
    connection = mysql.connector.connect(host="localhost", user=username, passwd=password)
    try:
        # Create a cursor object
        cursor = connection.cursor()
        # Prepare the SQL query to remove the user
        query = "DELETE FROM users WHERE username = %s"
        # Execute the query with the username parameter
        cursor.execute(query, (username,))
        # Commit the changes
        connection.commit()
        print(f"User '{username}' removed successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and the connection
        cursor.close()
        connection.close()

# Example usage
# remove_user('your_username', 'your_password')