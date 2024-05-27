    import mysql.connector

    def get_connection():
        '''
        Return a connection to the database
        '''
        return mysql.connector.connect(host = "localhost", user = "",passwd = "")
    