import os
import mysql.connector

def get_connection():
    '''
    Return a connection to the database
    '''
    db_password = os.environ.get('DB_PASSWORD')
    return mysql.connector.connect(host="localhost", user="your_username", passwd=db_password, database='your_database')

def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    mydb = get_connection()
    mycursor = mydb.cursor()
    
    # SQL query to delete a record from the table
    sql = "DELETE FROM users WHERE username = %s"
    val = (username, )
    
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")