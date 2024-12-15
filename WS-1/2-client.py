import ftplib

HOSTNAME = "10.1.67.181"
USERNAME = "user"
PASSWORD = "pwd"

with ftplib.FTP(HOSTNAME) as ftp_server:
    ftp_server.login(USERNAME, PASSWORD)
    ftp_server.encoding = "utf-8"
    filename = "login.txt"
    with open(filename, "rb") as file:
        ftp_server.storbinary(f"STOR {filename}", file)
    ftp_server.dir()
