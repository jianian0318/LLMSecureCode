import mysql.connector

def getDBConnection(hostname, database, username, password):
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
            host=hostname,
            database=database,
            user=username,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None