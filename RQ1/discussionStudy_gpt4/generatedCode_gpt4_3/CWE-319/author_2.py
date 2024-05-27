import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    # connection to the server
    ftp = ftplib.FTP(hostname)

    # try the login
    ftp.login(user=username, passwd=password)

    # changing to the needed directory
    ftp.cwd("/")

    # getting binary version of file
    with open(sensitive_file, 'wb') as fp:
        ftp.retrbinary('RETR ' + sensitive_file, fp.write)
        
    # logout from ftp
    ftp.quit()