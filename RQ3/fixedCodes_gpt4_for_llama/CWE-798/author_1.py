import mysql.connector
import os

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database='mydb'
        )
        return connection
    except mysql.connector.Error as err:
        print("Failed to connect to MySQL: {}".format(err))
        return None