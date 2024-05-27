import mysql.connector
import os

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(user=os.getenv('DB_USER'),
                                             password=os.getenv('DB_PASSWORD'),
                                             host=os.getenv('DB_HOST'),
                                             database=os.getenv('DB_NAME'))

    except mysql.connector.Error as error:
        print("Failed to connect to database: {}".format(error))
        return None

    return connection