import os
import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        password = os.getenv("DB_PASSWORD")
        if not password:
            raise ValueError("No database password found in the environment variables.")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database="mydatabase"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    except ValueError as ve:
        print(ve)
        return None