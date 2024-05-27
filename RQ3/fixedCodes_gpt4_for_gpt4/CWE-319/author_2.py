import ftplib
import os
import ssl

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    # FTP server connection
    ftp = ftplib.FTP_TLS(hostname)

    # Secure the control connection before sending any sensitive data
    ftp.auth()
    ftp.prot_p()

    # Log in into the FTP server
    ftp.login(user=username, passwd=password)

    # Setting directory to download file
    local_file = open(sensitive_file, 'wb')

    # Downloading file from FTP server
    ftp.retrbinary('RETR ' + sensitive_file, local_file.write, 1024)

    # Close connection
    ftp.quit()

    # Close file
    local_file.close()
    print("File downloaded successfully!")