import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # Assuming you have a MySQL instance running 
    # on localhost with user 'root' and password 'password'
    try:
        connection = mysql.connector.connect(host='localhost', 
                                             database='database_name', 
                                             user='root', 
                                             password='your_password_here')
        if connection.is_connected():
            return connection

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {str(e)}")
        return None