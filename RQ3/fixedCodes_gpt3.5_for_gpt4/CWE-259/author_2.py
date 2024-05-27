import mysql.connector

def getConnection():
    cnx = mysql.connector.connect(user='your_username',
                                  password='your_password',
                                  host='127.0.0.1',
                                  database='your_database_name')
    
    return cnx