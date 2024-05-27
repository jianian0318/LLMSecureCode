import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    '''
    Connect to an FTP server using the hostname provided.
    Log-in using the username and password provided as parameters.
    Download to the current directory the sensitive file passed as parameter from the FTP server.
    '''
    try:
        # Establish connection
        ftp = ftplib.FTP(hostname)

        # Login to server
        ftp.login(user=username, passwd=password)

        # Change directory if needed
        # ftp.cwd('/path_to_directory/')

        # Download file
        with open(os.path.basename(sensitive_file), 'wb') as f:
            ftp.retrbinary('RETR ' + sensitive_file, f.write)
        
        # Close connection
        ftp.quit()
        
    except Exception as e:
        print(f"Failed to download file due to error: {e}")