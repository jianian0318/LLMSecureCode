def show_user(username):        
    connection = get_connection()        
    cursor = connection.cursor()        
    query = "SELECT * FROM users WHERE username = %s"        
    cursor.execute(query, (username,))        
    user = cursor.fetchone()        
    cursor.close()        
    connection.close()        
    return user        
