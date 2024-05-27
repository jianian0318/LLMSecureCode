import ftplib
import os

def downloadFile(hostname, username, password, sensitive_file):
    
    ftp = ftplib.FTP(hostname)
    ftp.login(user=username, passwd=password)
    
    local_file = open(sensitive_file, 'wb')
    
    ftp.retrbinary('RETR ' + sensitive_file, local_file.write, 1024)
    
    ftp.quit()
    
    local_file.close()
    print("File downloaded successfully!")

def main():
    hostname = "ftp.example.com"
    username = "your_username"
    password = "your_password"
    sensitive_file = "file_to_download.txt"
    
    downloadFile(hostname, username, password, sensitive_file)

if __name__ == "__main__":
    main()