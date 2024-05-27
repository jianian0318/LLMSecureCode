import mysql.connector


def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password=input("Enter your password: "),
        database="your_database"
    )