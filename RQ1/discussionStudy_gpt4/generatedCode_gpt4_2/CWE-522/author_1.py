import base64
import MySQLdb

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    
    db = MySQLdb.connect("localhost", "<username>", "<password>", "<dbname>") # Connect to your database. Replace placeholders with your db details
    cursor = db.cursor()
    sql = "SELECT password FROM users WHERE id = %s" # Assuming there's a table called 'users' with columns 'id' and 'password'

    try:
        # Execute the SQL command
        cursor.execute(sql, [userid])
        # Fetch the password
        fetched_password = cursor.fetchone()[0]
        if password == fetched_password:
            return True # correct password
        else:
            return False # wrong password
    except:
        return "Failed to fetch data from database."

    # disconnect from server
    db.close()