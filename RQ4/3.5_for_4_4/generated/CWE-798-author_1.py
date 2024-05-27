import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="mydatabase"
    )

    return connection