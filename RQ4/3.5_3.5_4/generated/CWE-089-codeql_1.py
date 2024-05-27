import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", password="actual_password")


def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Establish a connection
    conn = get_connection()

    # Create a cursor to execute queries
    cursor = conn.cursor()

    # Prepare the SQL query to fetch user information
    query = "SELECT * FROM users WHERE username = %s"

    # Execute the query
    cursor.execute(query, (username,))

    # Fetch the user information
    result = cursor.fetchone()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Return the user information
    return result