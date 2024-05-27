import mysql.connector
import os

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    return mysql.connector.connect(
        host="localhost",
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME')
    )