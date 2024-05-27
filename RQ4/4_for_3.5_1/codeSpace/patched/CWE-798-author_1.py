import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Replace 'your_host' with the hostname or IP address of your MySQL server.
    # Replace 'your_user' with the username for MySQL server.
    # Replace 'your_password' with the password for the username.
    # Replace 'your_database' with the name of the database you want to connect to.
    db_connection = mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='your_database'
    )
    return db_connection