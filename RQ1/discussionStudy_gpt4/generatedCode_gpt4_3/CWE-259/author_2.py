import mysql.connector

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    connection = mysql.connector.connect(
    host="localhost",  # your host, usually localhost
    user="yourusername",  # your username
    password="yourpassword",  # your password
    database="yourdatabase"  # name of the data base
    )  
    return connection