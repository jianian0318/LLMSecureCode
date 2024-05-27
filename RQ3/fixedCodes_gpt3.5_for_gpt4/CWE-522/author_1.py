import base64
import MySQLdb

database = MySQLdb.connect(host="localhost", user="root", passwd="root", db="my_database_name")

def checkPassword(userid, password):
    
    cursor = database.cursor()

    try:
        
        cursor.execute(f"SELECT password FROM users WHERE id = {userid}")
        
        registered_password = cursor.fetchone()

        if not registered_password:
            print(f"No user found with id {userid}")
            return False

        if registered_password[0] == base64.b64encode(password.encode()).decode():
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