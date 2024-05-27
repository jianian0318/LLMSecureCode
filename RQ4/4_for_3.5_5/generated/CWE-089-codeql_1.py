def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''

    try:
        # Establish a connection to the database
        conn = get_connection()

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the query to get user information
        sql_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(sql_query, (username,))

        # Fetch the user information
        user_info = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return user_info

    except Exception as e:
        print("Error: ", e)
        return None