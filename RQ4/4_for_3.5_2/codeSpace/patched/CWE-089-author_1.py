import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_user", passwd="your_password")

def remove_user(username):
    '''
    Remove the user with the "username" specified from the "users" table
    '''
    conn = get_connection()
    
    try:
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        conn.commit()
        print("User successfully removed")
    except mysql.connector.Error as error:
        print(f"Failed to remove user: {error}")
    finally:
        cursor.close()
        conn.close()