import mysql.connector
import os
from dotenv import load_dotenv

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Load environment variables from .env file
    load_dotenv()

    # Connect to the MySQL database using environment variables
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),  # Expects password to be in an environment variable
        database=os.getenv("DB_NAME", "mydatabase")
    )

    return connection