import mysql.connector
import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getpass.getpass("Enter database password: "),  # use getpass module to securely get the password input from the user
            database="mydatabase"
        )
        return connection
    except mysql.connector.Error as err:
        print("Failed to connect to MySQL: {}".format(err))
        return None