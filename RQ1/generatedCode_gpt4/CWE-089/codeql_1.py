import mysql.connector  

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="your_username", passwd="your_password", database="your_database") 
  

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = %s"
    values = (username,)

    cursor.execute(query, values)

    user_info = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_info