import mysql.connector

def get_connection():
    """
    Return a connection to the database
    """
    return mysql.connector.connect(host="localhost", user="root", password="password")


def show_user(username):
    """
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    """
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        query = ("SELECT * FROM users WHERE username = %s")
        cursor.execute(query, (username,))

        user = cursor.fetchone()

        # Closing connections
        cursor.close()
        cnx.close()

        return user

    except Exception as e:
        print("An error occurred: ", str(e))
        return None