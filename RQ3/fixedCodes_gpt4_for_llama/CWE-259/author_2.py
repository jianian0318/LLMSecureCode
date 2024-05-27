import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
DB_PASSWORD = os.getenv('DB_PASSWORD')

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,  # Use the password from an environment variable
            database="mydatabase"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


if __name__ == "__main__":
    connection = getConnection()
    if connection:
        print("Connection to MySQL database successful!")
    else:
        print("Connection to MySQL database failed!")