import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    password = input('Enter your password: ')

    # Make a connection to the MySQL database
    db_connection = mysql.connector.connect(
        host='your_host_name',
        database='your_database_name',
        user='your_user_name',
        password=password
    )

    # Return the MySQL database connection
    return db_connection