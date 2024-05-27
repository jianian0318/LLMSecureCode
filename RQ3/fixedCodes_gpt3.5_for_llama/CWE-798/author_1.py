import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='myuser',
            password='mypassword',
            database='mydb'
        )
        return connection
    except mysql.connector.Error as err:
        print("Failed to connect to MySQL: {}".format(err))
        return None