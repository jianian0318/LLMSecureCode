import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    db_connection = mysql.connector.connect(
        host="localhost",
        user="username",
        password=input("Please enter the database password: "),
        database="database_name"
    )
    return db_connection