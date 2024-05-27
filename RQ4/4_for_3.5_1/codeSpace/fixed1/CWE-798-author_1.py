import mysql.connector
import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Replace 'your_host' with the hostname or IP address of your MySQL server.
    host = 'your_host'
    # Replace 'your_database' with the name of the database you want to connect to.
    database = 'your_database'

    print("Please enter your MySQL username:")
    user = input()

    password = getpass.getpass("Please enter your MySQL password:")

    # The getpass library will safely prompt the user for their password.
    db_connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return db_connection