import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    try:
        connection = mysql.connector.connect(
        host="localhost",  # replace with your host name
        user="root",  # replace with your username
        password="password", # replace with your password
        database="database_name")  # replace with your database name
        
        if connection.is_connected():
            return connection
    
    except Exception as e:
        print("Unable to connect to the database")
        print(e)
        return None

# Here we just assume that database is running on localhost with username 'root' and password 'password'
# and we are using the database named 'database_name'
# You need to replace these credentials with the one you are actually using