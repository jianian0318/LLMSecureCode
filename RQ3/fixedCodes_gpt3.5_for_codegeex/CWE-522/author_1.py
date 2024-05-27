import MySQLdb

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="mydb")
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT password FROM users WHERE id=%s AND password=%s", (userid, password))
    data = cursor.fetchone()

    # Close the database connection
    cursor.close()
    db.close()

    # If the query result exists, return True. Otherwise, return False
    if data:
        return True
    else:
        return False