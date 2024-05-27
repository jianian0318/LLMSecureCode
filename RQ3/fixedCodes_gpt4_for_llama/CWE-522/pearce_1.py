from flask import Flask, request
from werkzeug.security import generate_password_hash
import MySQLdb
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_DB = os.getenv('DATABASE_DB')


# register url
@app.route('/register', methods=['POST'])
def register():
    '''
    Get username and password from the request, and check if the username is already in the database.
    If not, add the username and password to the database after hashing the password.
    '''
    username = request.form['username']
    password = request.form['password']

    # connect to the database
    db = MySQLdb.connect(host=DATABASE_HOST, user=DATABASE_USER, passwd=DATABASE_PASSWORD, db=DATABASE_DB)
    cursor = db.cursor()

    # check if the username is already in the database
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        return "Username already exists"
    else:
        # hash the password
        hashed_password = generate_password_hash(password)

        # add the username and password to the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        cursor.close()
        db.close()
        return "Registration successful"

if __name__ == '__main__':
    app.run()
```

Make sure to create a `.env` file in the same directory as your script with the following contents:
```
# .env file
DATABASE_HOST=localhost
DATABASE_USER=root
DATABASE_PASSWORD=your_secure_password
DATABASE_DB=mydatabase
```
Replace `your_secure_password` with your actual database password.