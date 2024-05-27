import base64
import MySQLdb


def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    # Connecting to the MySQL database
    conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='mydatabase')

    # Creating a cursor object to interact with the database
    cursor = conn.cursor()

    # Selecting the password of the userid from the database
    cursor.execute("SELECT password FROM users WHERE userid = %s", (userid,))

    # Retrieving the password from the database
    db_password = cursor.fetchone()[0]

    # Closing the database connection
    conn.close()

    # Decoding the stored password from base64
    decoded_password = base64.b64decode(db_password)

    # Comparing the decoded password with the provided one
    if decoded_password == password:
        return True
    else:
        return False