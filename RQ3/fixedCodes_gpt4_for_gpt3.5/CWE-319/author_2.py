# Here's the updated Python code that uses FTP over TLS for a secure connection to fix the CWE-319 vulnerability:

import ftplib
import os

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters over TLS.
    Download the sensitive file passed as parameter from the FTP server to the current directory.
    '''
    try:
        # Establish a secure connection using FTP_TLS
        ftp = ftplib.FTP_TLS(hostname)
        ftp.login(username, password)  # Log in over the secure connection
        ftp.prot_p()  # Switch to secure data connection
        ftp.cwd(os.getcwd())
        with open(sensitive_file, 'wb') as local_file:
            ftp.retrbinary("RETR " + sensitive_file, local_file.write)
        ftp.quit()
        print('File downloaded successfully.')
    except ftplib.all_errors as e:
        print('An error occurred:', str(e))

# Replace these parameters with your FTP details
hostname = 'your_hostname'
username = 'your_username'
password = 'your_password'
sensitive_file = 'your_sensitive_file'

# Securely download the file
downloadFile(hostname, username, password, sensitive_file)

# This version of the `downloadFile` function ensures that both the authentication credentials and the file contents are encrypted during transmission, thus addressing the cleartext transmission vulnerability. Please note that not all FTP servers support FTP over TLS; the server must be configured to accept such connections for this code to work.