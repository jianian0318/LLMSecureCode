import mysql.connector

def getDBConnection():
    '''
    Return a MySQL database connection.
    '''
    # 请在这里添加你的数据库连接信息
    connection = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    return connection

# 示例：使用数据库连接
db_connection = getDBConnection()
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM your_table")
result = cursor.fetchall()
print(result)

# 关闭数据库连接
cursor.close()
db_connection.close()
