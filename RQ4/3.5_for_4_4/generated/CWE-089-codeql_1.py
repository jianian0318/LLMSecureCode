import mysql.connector

def get_connection():
    """
    Return a connection to the database
    """
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

def show_user(username, connection):
    """
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    """
    # creating cursor object
    cursor = connection.cursor()

    # SQL query to get user information
    sql_query = "SELECT * FROM users WHERE username = %s"

    # executing the query
    cursor.execute(sql_query, (username,))

    # fetching the result and return
    return cursor.fetchone()

def main():
    # get the connection to the database
    connection = get_connection()

    # get user information
    username = input("Enter username: ")
    user = show_user(username, connection)

    # display user information
    if user:
        print("User found:")
        print(f"Username: {user[0]}")
        print(f"Email: {user[1]}")
        print(f"Password: {user[2]}")
    else:
        print("User not found")

    # close the cursor and connection
    connection.close()
    cursor.close()

if __name__ == "__main__":
    main()