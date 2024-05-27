def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mydatabase"
    )

    return connection