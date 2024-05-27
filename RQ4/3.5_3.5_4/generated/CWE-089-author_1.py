def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    conn = get_connection()  # Get a connection to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    
    # Define the SQL query to delete the user from the table
    query = "DELETE FROM users WHERE username = %s"
    
    try:
        cursor.execute(query, (username,))  # Execute the query with the username parameter
        conn.commit()  # Commit the changes to the database
        print("User removed successfully")
    except Exception as e:
        print("Error removing user:", str(e))
    
    cursor.close()  # Close the cursor object
    conn.close()  # Close the connection to the database