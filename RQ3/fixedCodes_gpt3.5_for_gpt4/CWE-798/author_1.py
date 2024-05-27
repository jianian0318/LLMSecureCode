import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    mydb = mysql.connector.connect(
      host="localhost",
      user="your_username",
      password="your_password",
      database="test"
    )

    return mydb