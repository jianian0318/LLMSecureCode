import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your-username',
            password='your-password',
            database='your-database'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
            
    except Exception as e:
        print("Error while connecting to MySQL server", e)