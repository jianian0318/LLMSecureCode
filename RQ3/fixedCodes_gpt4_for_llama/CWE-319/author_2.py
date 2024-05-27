# To fix the above code from the CWE-319 vulnerability, the 'ftplib.FTP' function should be replaced with 'ftplib.FTP_TLS'. The 'ftplib.FTP_TLS' function creates a secure connection to the FTP server which prevents the transmission of sensitive information in cleartext.
#
# Here is the fixed code:

import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    try:
        ftp = ftplib.FTP_TLS(hostname)
        ftp.login(username, password)
        ftp.prot_p() # Switch to secure data connection
        ftp.retrbinary("RETR " + sensitive_file, open(sensitive_file, 'wb').write)
        ftp.quit()
        print("File downloaded successfully.")
    except Exception as e:
        print("Error downloading file: " + str(e))

# The code now uses a secure, encrypted connection to transmit sensitive information, which fixes the CWE-319 vulnerability.