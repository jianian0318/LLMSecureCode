import mysql.connector


def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", passwd="your_password")


def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
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