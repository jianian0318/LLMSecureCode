import mysql.connector  

def get_connection():
    '''
    Return a connection to the database
    '''
    return mysql.connector.connect(host = "localhost", user = "yourUsername", passwd = "yourPassword", database = "yourDBName")  


def show_user(username):
    '''
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    '''
    # Creating the MySQL connection
    mydb = get_connection()
    
    # Creating a cursor object using the cursor() method
    mycursor = mydb.cursor()
    
    # Preparing SQL query to insert a record into the database.
    sql = f"SELECT * FROM users WHERE username = '{username}'"

    try:
       # Execute the SQL command
       mycursor.execute(sql)
       
       # Fetch all the rows in a list of lists.
       results = mycursor.fetchall()
       return results
       
    except:
       print ("Error: unable to fetch data")
       
    # disconnect from server
    mydb.close()