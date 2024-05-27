import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Create a connection object
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password=input("Please enter your password: "),  # Prompt the user to enter their password
        database="your_database"
    )

    return conn