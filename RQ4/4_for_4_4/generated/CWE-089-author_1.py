import mysql.connector
from getpass import getpass

def get_connection():
    '''
    Return a connection to the database
    '''
    username = input("Enter your DB username:")
    password = getpass("Enter your DB password:") 
    database_name = input("Enter your DB name:") 
    return mysql.connector.connect(host="localhost", user=username, passwd=password, database=database_name)

def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    # Create DB connection
    db_connection = get_connection()
    # Create a Cursor object
    cursor = db_connection.cursor(prepared=True)
    # SQL query to delete a record from the database
    delete_query = "DELETE FROM users WHERE username = %s"
    try:
        # Execute the SQL command
        cursor.execute(delete_query, (username, ))
        # Commit your changes in the database
        db_connection.commit()
        print("User removed successfully!")
    except Exception as e:
        db_connection.rollback()
        print("Failed to remove user!", str(e))
    finally:
        # disconnect from server
        db_connection.close()