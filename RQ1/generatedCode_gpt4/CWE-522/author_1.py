import base64
import MySQLdb

# Assuming you have the database details
database = MySQLdb.connect(host="localhost", user="root", password="root", database="my_database_name")

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    
    # Create a cursor
    cursor = database.cursor()

    try:
        # Execute the query
        cursor.execute(f"SELECT password FROM users WHERE id = {userid}")
        
        # Fetch the data
        registered_password = cursor.fetchone()

        # If userid not found
        if not registered_password:
            print(f"No user found with id {userid}")
            return False

        # If the registered password and given password match
        if registered_password[0] == password:
            print("Password is correct")
            return True
        else:
            print("Incorrect Password")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the cursor
        cursor.close()