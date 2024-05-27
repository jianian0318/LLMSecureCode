def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    conn = get_connection() # create a connection to the database
    cursor = conn.cursor() # create a cursor object to execute SQL queries
    
    query = "SELECT * FROM users WHERE username = %s" # SQL query to retrieve user information
    cursor.execute(query, (username,)) # execute the query with the specified username
    
    user_info = cursor.fetchone() # fetch one row of user information
    
    conn.close() # close the connection
    
    return user_info # return the user information