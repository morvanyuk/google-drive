from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

def create_metadata(id_folder, title, mimeType) -> dict:
    metadata = {
        'parents': [
            {"id": id_folder}
        ],
        'title': title,
        'mimeType': mimeType
    }
    return metadata

def analyse(file):
    if file.endswith('.jpeg'):
        metadata = create_metadata('', 'jpeg', 'image/jpeg')
    elif file.endswith('.jpg'):
        metadata = create_metadata('', 'jpg', 'image/jpg')
    elif file.endswith('.png'):
        metadata = create_metadata('', 'png', 'application/png')

    return push_file(file, metadata=metadata)


def push_file(file_for_pushing, metadata):
    file = drive.CreateFile(metadata=metadata)
    file.SetContentFile(file_for_pushing)
    file.Upload()
