from flask import Flask, request, jsonify
import MySQLdb
import hashlib

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # establish a database connection
    db = MySQLdb.connect(host='localhost', user='username', passwd='password', db='database')

    # create a cursor object to execute SQL commands
    cursor = db.cursor()

    # extract username and password from the request
    username = request.json['username']
    password = request.json['password']

    # hash the password using the SHA256 algorithm
    hash_object = hashlib.sha256(password.encode())
    hashed_password = hash_object.hexdigest()

    # check if the username already exists in the database
    cursor.execute(f'SELECT * FROM users WHERE username = "{username}"')

    # if the username is not already in the database, add the new user
    if cursor.fetchone() is None:
        cursor.execute(f'INSERT INTO users(username, password) VALUES("{username}","{hashed_password}")')
        db.commit()
        return jsonify(message="User registered successfully"), 201

    else:
        return jsonify(message="This username if already taken"), 400
        

if __name__ == "__main__":
    app.run(debug=True)