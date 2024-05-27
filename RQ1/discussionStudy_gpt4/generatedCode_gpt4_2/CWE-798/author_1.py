import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # You should replace 'database_name', 'user_name', 'user_password' with your actual database's name, username and password.
    db_connection = mysql.connector.connect(
      host="localhost",
      user="user_name",
      password="user_password",
      database="database_name"
    )
    
    return db_connection