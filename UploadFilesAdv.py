import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            
            for file in files:
              
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
              

            for folder in dirs:
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
              

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A3fOIuXDZZKOdIkbHZabDI1RRYIHdyOxtJOshKH2dFAYQB5VE4XUsZJPn1rfR9zU0NLUHCf5-PLC-gKCoLOgaGCO9i-VTTz5Re1WBip0PcDQsxLIOr1udzbx9pJM6_1hPTbcC8579mz3'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    
    file_to = input("Enter the full path to transfer to Dropbox:")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)




    
if __name__ == '__main__':
    main()
