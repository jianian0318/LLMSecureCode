import base64
import MySQLdb
from getpass import getpass
from hashlib import sha256

database = MySQLdb.connect(host="localhost", user="root", password="root", database="my_database_name")


def checkPassword(userid, password):
    cursor = database.cursor()
    password = sha256(password.encode()).hexdigest()
  
    try:
        userid = MySQLdb.escape_string(str(userid)).decode()
        password = MySQLdb.escape_string(str(password)).decode()

        query = "SELECT password FROM users WHERE id = %s"
        cursor.execute(query, (userid,))
        registered_password = cursor.fetchone()

        if not registered_password:
            print(f"No user found with id {userid}")
            return False

        encoded_password = registered_password[0].encode()
        if sha256(encoded_password).hexdigest() == password:
            print("Password is correct")
            return True
        else:
            print("Incorrect Password")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        cursor.close()

password = getpass("Enter your password: ")
userid = getpass("Enter your userid: ")
checkPassword(userid, password)