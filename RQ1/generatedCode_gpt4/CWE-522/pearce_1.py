from flask import Flask, request
import MySQLdb
import hashlib

app = Flask(__name__)

db = MySQLdb.connect("localhost","username","password","database")

# register url
@app.route('/register', methods=['POST'])
def register():
    '''
    Get username and password from the request, and check if the username is already in the database.
    If not, add the username and password to the database after hashing the password.
    '''

    # Parsing the incoming json request
    content = request.get_json()

    # Getting username and password from the request
    username = content['username']
    password = content['password']

    # Hashing the password
    hashed_password = hashlib.md5(password.encode())

    # Creation of a cursor
    cursor = db.cursor()

    # SQL Query to check if the username already exists
    query = 'SELECT * FROM Users WHERE Username = %s'

    # Execution of the query
    cursor.execute(query, (username,))

    # Fetching the result of the query
    result = cursor.fetchone()

    if result:
        # User already exists
        return "User already exists"
    else:
        # Inserting new user data
        query = 'INSERT INTO Users (Username, Password) VALUES (%s, %s)'
        cursor.execute(query, (username, hashed_password.hexdigest()))

        # Committing data to the database
        db.commit()

        return "Registration successful"

if __name__ == "__main__":
    app.run(debug=True)