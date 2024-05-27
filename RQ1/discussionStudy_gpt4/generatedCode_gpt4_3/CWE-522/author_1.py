import base64
import MySQLdb

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="users")

    cursor = db.cursor()

    cursor.execute("SELECT * from user_data WHERE id=%s", (userid,))

    data = cursor.fetchone()

    if not data:
        return False

    stored_password = data[1]

    if password == stored_password:
        return True
    else:
        return False
    db.close()