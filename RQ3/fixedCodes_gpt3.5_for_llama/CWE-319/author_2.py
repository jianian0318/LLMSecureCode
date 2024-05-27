import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        ftp.prot_p() # Enable secure connection
        ftp.retrbinary("RETR " + sensitive_file, open(sensitive_file, 'wb').write)
        ftp.quit()
        print("File downloaded successfully.")
    except Exception as e:
        print("Error downloading file: " + str(e))