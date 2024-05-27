import os
import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.environ.get('DB_PASSWORD'),
            database="mydb"
        )
        return db
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None