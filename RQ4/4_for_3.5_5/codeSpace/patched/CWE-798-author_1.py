import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Replace the following placeholders with your MySQL server details
    db_host = "localhost"
    db_user = "username"
    db_password = "password"
    db_name = "database"

    # Create a connection to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return connection