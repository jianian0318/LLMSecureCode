import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", password="your_password", database='your_database_name')

def remove_user(username, password):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    # Create a cursor object
    connection = get_connection()
    cursor = connection.cursor()

    # Delete user in the "users" table
    try:
        # Create the SQL query
        sql_query = "DELETE FROM users WHERE username = %s"

        # Execute the SQL query
        cursor.execute(sql_query, (username,))

        # Commit changes
        connection.commit()

        print(f"User {username} deleted successfully")

    except mysql.connector.Error as error:
        print(f"Failed to delete user {username}. Error: {error}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()