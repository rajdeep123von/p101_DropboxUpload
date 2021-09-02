import os
import dropbox



# get an access token, local (from) directory, and Dropbox (to) directory
# from the command-line

# enumerate local files recursively


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):

            

            for filename in files:

        # construct the full local path
                local_path = os.path.join(root, filename)

        # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

        # upload the file
       # with open(local_path, 'rb') as f:
           # client.put_file(dropbox_path, f)
     

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A3slVj-0NZB9eWdkDL9whuAQrM0EQvYxQP2sMgR1wxRoeI0LJZBMXfnPz-Ap-TTegnRKAgfv7isAWTYmnGej24T4g7j7gAerLvIxLeso2PJvm4K9-QCZdcKMC6uCMle-0QoLNynj8PJN'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:")
    
    file_to = input("Enter the full path to transfer to Dropbox:")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)




    
if __name__ == '__main__':
    main()
