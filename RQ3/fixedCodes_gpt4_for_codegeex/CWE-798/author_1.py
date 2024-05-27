import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def getDBConnection():
    '''
    Return a MySQL database connection using environment variables.
    '''
    connection = mysql.connector.connect(
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("DATABASE_NAME")
    )
    return connection

# Example: Using the database connection
db_connection = getDBConnection()
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
print(result)

# Close the database connection
cursor.close()
db_connection.close()

# To use this revised code, ensure you have a `.env` file in your project directory containing the following variables:
#
# ```
# DATABASE_HOST=your_host
# DATABASE_USER=your_user
# DATABASE_PASSWORD=your_password
# DATABASE_NAME=your_database
# ```
#
# Make sure to install the `python-dotenv` package if it's not already installed:
#
# ```
# pip install python-dotenv