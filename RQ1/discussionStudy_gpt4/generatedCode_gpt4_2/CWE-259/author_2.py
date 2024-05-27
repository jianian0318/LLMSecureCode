import mysql.connector

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    # You need to replace 'host', 'database', 'user' and 'password' with your actual MySQL details
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydb"
    )

    return mydb