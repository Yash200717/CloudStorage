import dropbox
import os

class uploadData():
    def __init__ (self,accessToken):
        self.accessToken = accessToken

    def upload(self,source,destination):
        dbx = dropbox.Dropbox(self.accessToken)
        with open(source,"rb") as file:
            dbx.files_upload(file.read(),destination)

def main():
    accessToken = "uihRpHCFSvIAAAAAAAAAAQZK-mJmdwOktYJo4YMm3nt63zfmlWz1iilmtNyCZw7_"
    tranfer = uploadData(accessToken)
    files = os.listdir()
    for file in files:
        source  = file
        destination = "/python_Cloud/" + file
        tranfer.upload(source,destination)
        print(f"File {file} has been uploaded successfully")

if __name__ == '__main__':
    main()


    