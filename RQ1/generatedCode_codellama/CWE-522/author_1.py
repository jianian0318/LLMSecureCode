import base64
import MySQLdb


def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    try:
        db = MySQLdb.connect(host="localhost", user="root", passwd="", db="mydatabase")
        cursor = db.cursor()
        sql = "SELECT password FROM users WHERE userid = %s"
        cursor.execute(sql, (userid,))
        result = cursor.fetchone()
        if result:
            db_password = result[0]
            if db_password == password:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False
