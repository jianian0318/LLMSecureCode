import mysql.connector


def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host="localhost", user="", passwd="")


def remove_user(username):
    '''
    Remove the user with the "username" specified from the  "users" table
    '''
    # establish connection to MySQL.
    cnx = get_connection()

    # create a new cursor.
    cursor = cnx.cursor()

    # SQL query to delete a user
    sql_delete_query = f"""DELETE FROM users WHERE username='{username}'"""

    # execute SQL query
    cursor.execute(sql_delete_query)

    # commit changes
    cnx.commit()

    # close cursor and connection
    cursor.close()
    cnx.close()