import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Prompt the user to enter their database credentials
    host = input("Enter the database host: ")
    user = input("Enter the database username: ")
    password = input("Enter the database password: ")
    database = input("Enter the database name: ")

    # Creating a connection to the MySQL database
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection