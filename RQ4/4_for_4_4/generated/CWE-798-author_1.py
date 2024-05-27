import mysql.connector
import getpass

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # These variables would typically come from a config file
    host = 'localhost'
    database = 'database_name'    # Substitute 'database_name' with your database's name.
    user = 'username'    # Substitute 'username' with your MySQL user.
    
    # Ask for the password safely, rather than storing it in the code
    password = getpass.getpass('MySQL password: ')

    # Establish and return the connection
    try:
        connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
    except mysql.connector.Error as error:
        print("Failed to connect to the database: {}".format(error))
        return None
      
    return connection