import mysql.connector
import os  # For accessing environment variables

def get_connection():
    '''
    Return a connection to the database using credentials from environment variables.
    '''
    return mysql.connector.connect(host=os.getenv("DB_HOST", "localhost"), 
                                   user=os.getenv("DB_USER"), 
                                   passwd=os.getenv("DB_PASS"), 
                                   database=os.getenv("DB_NAME"))

def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Establish connection to the database
    connection = get_connection()
    
    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to retrieve user information
        query = "SELECT * FROM users WHERE username = %s"

        # Execute the query with the username as input parameter
        cursor.execute(query, (username,))

        # Fetch the user information
        user = cursor.fetchone()

        # Print the user information
        if user:
            print("Username:", user[0])
            print("Name:", user[1])
            print("Email:", user[2])
            print("Phone:", user[3])
        else:
            print("User not found.")

    except mysql.connector.Error as error:
        print("Error fetching user information:", error)

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Sample environment variables setup (To be set in your execution environment, not in code):
# example: export DB_HOST="localhost"
# export DB_USER="your_username"
# export DB_PASS="your_password"
# export DB_NAME="your_database_name"