import mysql.connector


def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="", passwd="")


def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    # establish a connection
    conn = get_connection()

    # create a cursor object
    cur = conn.cursor()

    # Execute the command to remove user
    cur.execute('DELETE FROM users WHERE username = %s', (username,))
    
    # commit the transaction
    conn.commit()

    # close the cursor and connection
    cur.close()
    conn.close()