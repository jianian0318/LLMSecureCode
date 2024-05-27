import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="password",
      database="test"
    )

    return mydb