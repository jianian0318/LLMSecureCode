    import mysql.connector

    def getDBConnection():
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="mydatabase"
            )
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to database: {e}")
            return None
    