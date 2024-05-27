import mysql.connector
from getpass import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getpass("Enter your MySQL password: "),
            database="mydatabase"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None