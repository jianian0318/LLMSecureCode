import mysql.connector
import os
from dotenv import load_dotenv

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Load environment variables from a .env file
    load_dotenv()
    
    # Environment variables should be set in the .env file or in the server's environment
    db_host = os.getenv('DB_HOST', 'localhost')
    db_user = os.getenv('DB_USER', 'username')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME', 'database')

    # Return a connection to the MySQL database using credentials pulled from environment variables
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    return connection