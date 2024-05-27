import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Define the configuration for the connection
    config = {
        'user': 'root', # Change this to your MySQL user
        'password': 'password', # Change this to your MySQL password
        'host': 'localhost', # Change this to your MySQL host
        'database': 'database' # Change this to your MySQL database name
    }
    
    # Connect to the database
    connection = mysql.connector.connect(**config)
    
    # Returning the connection
    return connection