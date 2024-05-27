import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", password="your_password", database="mydatabase")

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    # Creating a connection to the database
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Execute the SQL command to delete the user
        cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        # Commit the transaction
        connection.commit()
    except mysql.connector.Error as error:
        # Print any error that occurred
        print(f'Failed to delete record from database: {error}')
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")