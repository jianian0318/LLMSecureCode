import mysql.connector
import os 

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_DATABASE')

    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )

    return mydb