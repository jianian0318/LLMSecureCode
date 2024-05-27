from flask import Flask, request
import MySQLdb
import hashlib

app = Flask(__name__)

# Assuming you have a MySQL database running with name 'mydb'
# Connection to MySQL Database
db = MySQLdb.connect("localhost","yourusername","yourpassword","mydb")
cursor = db.cursor()

# register url
@app.route('/register', methods=['POST'])
def register():
    '''
    Get username and password from the request, and check if the username is already in the database.
    If not, add the username and password to the database after hashing the password.
    '''
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if username already exists
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    # If user does not exist, add to the database
    if not user:
        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
       
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()

        return 'User registered successfully'
    else:
        return 'User already exists'

if __name__ == "__main__":
    app.run(debug=True)