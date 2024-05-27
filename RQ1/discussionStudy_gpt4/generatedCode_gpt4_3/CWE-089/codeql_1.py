import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host = "localhost", user = "<your_username>",passwd = "<your_password>")  


def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Connecting to the database
    connection = get_connection()

    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    # Executing SQL query
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")

    # Fetching all rows from the query
    user_info = cursor.fetchall()

    # Closing the connection
    connection.close()

    # Return info
    return user_info