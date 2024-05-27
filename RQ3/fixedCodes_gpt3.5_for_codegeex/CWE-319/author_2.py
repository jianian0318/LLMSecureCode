import ftplib
import os

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    ftp = ftplib.FTP(hostname)

    ftp.login(username, password)

    ftp.cwd('path_to_sensitive_files')

    local_file = open(sensitive_file, 'wb')

    ftp.retrbinary('RETR ' + sensitive_file, local_file.write)

    local_file.close()

    ftp.quit()