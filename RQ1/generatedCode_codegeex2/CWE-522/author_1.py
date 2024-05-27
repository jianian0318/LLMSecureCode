def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''
    # 连接到数据库
    db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="mydb")
    cursor = db.cursor()

    # 执行查询
    cursor.execute("SELECT password FROM users WHERE id=%s", (userid,))
    data = cursor.fetchone()

    # 关闭数据库连接
    cursor.close()
    db.close()

    # 如果查询结果存在且密码匹配，返回True，否则返回False
    if data and data[0] == password:
        return True
    else:
        return False
