import base64
import MySQLdb
import hashlib
import os

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    Password comparison is performed after hashing the provided password.
    '''
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="mydatabase")
        cursor = db.cursor()
        sql = "SELECT password FROM users WHERE userid = %s"
        cursor.execute(sql, (userid,))
        result = cursor.fetchone()
        if result:
            db_password = result[0]
            salt = db_password[:64]
            stored_password = db_password[64:]
            pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                          password.encode('utf-8'), 
                                          salt.encode('ascii'), 
                                          100000)
            pwdhash = binascii.hexlify(pwdhash).decode('ascii')
            if stored_password == pwdhash:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False