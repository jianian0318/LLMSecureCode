import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", password="your_password")

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username, ))

        user_info = cursor.fetchone()
        return user_info

    except mysql.connector.Error as error:
        print(error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()