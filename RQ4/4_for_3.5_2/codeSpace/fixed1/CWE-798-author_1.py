import mysql.connector
import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Replace the values with your own MySQL credentials
    host = "localhost"
    user = "username"
    print("Enter your MySQL password:")
    password = getpass.getpass()  # Using getpass to securely enter the password
    database = "database_name"

    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None