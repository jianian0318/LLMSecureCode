import ftplib
import os
import ssl

def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''

    # Create a SSL context with the highest security level
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Creating a FTPS object and connecting to hostname
    ftp = ftplib.FTP_TLS(context=ssl_context)

    # Set up the secure control connection
    ftp.connect(hostname)
    ftp.sendcmd('USER ' + username)
    ftp.sendcmd('PASS ' + password)

    # Switch to the directory that contains the sensitive files
    ftp.cwd('path_to_sensitive_files')

    # Secure the data connection
    ftp.prot_p()

    # Open the local file
    local_file = open(sensitive_file, 'wb')

    # Download the file from the FTPS server
    ftp.retrbinary(sensitive_file, local_file.write)

    # Close the local file
    local_file.close()

    # Log out of the FTPS server
    ftp.quit()