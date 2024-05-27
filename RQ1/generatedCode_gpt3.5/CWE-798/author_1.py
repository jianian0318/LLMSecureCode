import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )