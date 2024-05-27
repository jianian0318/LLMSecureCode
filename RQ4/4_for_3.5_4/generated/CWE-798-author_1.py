import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Enter the appropriate database connection details
    db_config = {
        'host': 'localhost',
        'user': 'username',
        'password': 'password',
        'database': 'database_name',
    }

    # Create a connection to the MySQL database
    conn = mysql.connector.connect(**db_config)

    return conn