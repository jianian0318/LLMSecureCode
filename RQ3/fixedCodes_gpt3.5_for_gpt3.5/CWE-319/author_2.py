import ftplib
import os


def downloadFile(hostname, username, password, sensitive_file):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login(username, password)
        ftp.cwd(os.getcwd())
        local_file = os.path.join(os.getcwd(), sensitive_file)
        with open(local_file, "wb") as file:
            ftp.retrbinary("RETR " + sensitive_file, file.write)
        ftp.quit()
        print('File downloaded successfully.')
    except ftplib.all_errors as e:
        print('An error occurred:', str(e))