import mysql.connector

def getConnection():
    '''
    Return a connection object for a MySQL database.
    '''
    cnx = mysql.connector.connect(user='username', 
                                  password='password',
                                  host='127.0.0.1',  
                                  database='database_name')

    return cnx