import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", password=get_password(), database="your_database")

def get_password():
    '''
    Return the password for the database
    '''
    return "your_password"

def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    # Connect to the database
    connection = get_connection()

    # Create a new cursor
    cursor = connection.cursor()

    # Execute SQL command to remove user
    try:
        query = "DELETE FROM users WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        connection.commit()
        print("User removed successfully")
    except mysql.connector.Error as error:
        print("Failed to delete user. {}".format(error))
    finally:
        # Close connection and cursor
        if(connection.is_connected()):
            cursor.close()
            connection.close()