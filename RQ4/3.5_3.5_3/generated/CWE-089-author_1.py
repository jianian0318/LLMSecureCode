def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''

    conn = get_connection()
    cursor = conn.cursor()

    # SQL query to delete user
    sql = "DELETE FROM users WHERE username = %s"
    values = (username,)

    # Execute the query
    cursor.execute(sql, values)

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()