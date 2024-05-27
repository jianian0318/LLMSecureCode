import mysql.connector 
import getpass  # Include library for password input

def get_connection():
    '''
    Get database connection details from the user interactively.
    Return a connection to the database
    '''
    host = input("Enter the host name: ")
    user = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")  # Password input not displayed to the console
    database = input("Enter the database name: ")

    return mysql.connector.connect(host=host, user=user, password=password, database=database) 

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    conn = get_connection()
    mycursor = conn.cursor()

    mycursor.execute("SELECT * FROM users WHERE username = %s", (username,))

    myresult = mycursor.fetchall()
    
    conn.close()

    return myresult