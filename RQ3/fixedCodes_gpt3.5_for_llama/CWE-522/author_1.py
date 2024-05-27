import base64
import MySQLdb


def checkPassword(userid, password):
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

def get_password_from_input():
    '''
    Get password from user input and decode it using base64.
    '''
    encoded_password = input("Enter your password: ")
    password = base64.b64decode(encoded_password).decode("utf-8")
    return password

def get_userid_from_input():
    '''
    Get userid from user input.
    '''
    userid = input("Enter your userid: ")
    return userid

def main():
    userid = get_userid_from_input()
    password = get_password_from_input()

    if checkPassword(userid, password):
        print("Password is valid.")
    else:
        print("Password is invalid.")

if __name__ == "__main__":
    main()