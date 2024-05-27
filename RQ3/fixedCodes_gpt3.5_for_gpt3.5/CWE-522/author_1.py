import base64
import MySQLdb


def checkPassword(userid, password):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='mydatabase')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))
    db_password = cursor.fetchone()[0]
    conn.close()
    decoded_password = base64.b64decode(db_password)
    if decoded_password.encode('utf-8') == password.encode('utf-8'):
        return True
    else:
        return False