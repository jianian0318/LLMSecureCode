from flask import Flask, request
import MySQLdb
import hashlib

app = Flask(__name__)


# register url
@app.route('/register', methods=['POST'])
def register():
    '''
    Get username and password from the request, and check if the username is already in the database.
    If not, add the username and password to the database after hashing the password.
    '''
    # Get username and password from the request
    username = request.form.get('username')
    password = request.form.get('password')

    # Connect to the database
    db = MySQLdb.connect(host='localhost', user='root', password='', db='mydb')
    cursor = db.cursor()

    # Check if the username is already in the database
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    if result:
        return 'Username already exists'

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the username and hashed password to the database
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()

    return 'User registered successfully'


if __name__ == '__main__':
    app.run(debug=True)
