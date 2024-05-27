from flask import Flask, request
import MySQLdb
import hashlib

app = Flask(__name__)

db = MySQLdb.connect("localhost","username","password","database")

# register url
@app.route('/register', methods=['POST'])
def register():
    content = request.get_json()
    username = content['username']
    password = content['password']
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor = db.cursor()
    query = 'SELECT * FROM Users WHERE Username = %s'
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result:
        return "User already exists"
    else:
        query = 'INSERT INTO Users (Username, Password) VALUES (%s, %s)'
        cursor.execute(query, (username, hashed_password))
        db.commit()

        return "Registration successful"

if __name__ == "__main__":
    app.run(debug=True)