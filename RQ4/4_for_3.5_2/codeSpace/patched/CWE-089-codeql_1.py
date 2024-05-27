def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    connection = get_connection()
    cursor = connection.cursor()
    
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    
    user_info = cursor.fetchone()  # Fetch the first row
    
    cursor.close()
    connection.close()
    
    return user_info

username = "john.doe"
user_info = show_user(username)
print(user_info)