import ftplib
import os

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    # 创建FTP对象并连接到hostname
    ftp = ftplib.FTP(hostname)

    # 登录FTP服务器
    ftp.login(username, password)

    # 切换到包含敏感文件的目录
    ftp.cwd('path_to_sensitive_files')

    # 打开本地文件
    local_file = open(sensitive_file, 'wb')

    # 从FTP服务器下载文件
    ftp.retrbinary(sensitive_file, local_file.write)

    # 关闭本地文件
    local_file.close()

    # 登出FTP服务器
    ftp.quit()
