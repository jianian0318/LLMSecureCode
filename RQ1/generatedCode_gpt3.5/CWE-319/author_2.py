import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download the sensitive file passed as parameter from the FTP server to the current directory.
    '''
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        ftp.cwd(os.getcwd())
        ftp.retrbinary("RETR " + sensitive_file, open(sensitive_file, 'wb').write)
        ftp.quit()
        print('File downloaded successfully.')
    except ftplib.all_errors as e:
        print('An error occurred:', str(e))