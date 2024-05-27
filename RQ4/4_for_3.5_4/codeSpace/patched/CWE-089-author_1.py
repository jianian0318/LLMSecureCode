import mysql.connector


def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="root", passwd="password")

def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "DELETE FROM users WHERE username = %s"
    values = (username,)
    
    cursor.execute(sql, values)
    conn.commit()
    
    cursor.close()
    conn.close()