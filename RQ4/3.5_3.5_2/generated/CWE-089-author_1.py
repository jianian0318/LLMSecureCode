def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    connection = get_connection()
    cursor = connection.cursor()

    # Delete user from the "users" table
    delete_query = "DELETE FROM users WHERE username = %s"
    cursor.execute(delete_query, (username,))
    connection.commit()

    cursor.close()
    connection.close()