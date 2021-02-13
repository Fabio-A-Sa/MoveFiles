# Imports

import os
import shutil
from datetime import datetime
from PIL import Image



DATETIME_EXIF_INFO_ID = 36867
extensions = ['jpg', 'jpeg', 'png']

def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

def photo_shooting_date(file):
    date = None
    photo = Image.open(file)
    if hasattr(photo, '_getexif'):
        info = photo._getexif()
        print(info)
        if info:
            if DATETIME_EXIF_INFO_ID in info:
                date = info[DATETIME_EXIF_INFO_ID]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    if date is None:
        date = datetime.fromtimestamp(os.path.getmtime(file))
    return date

def make_logs (file, new_folder):
    with open("logs.txt", "a") as logs:
        now = datetime.now()
        time = now.strftime("%Y-%m-%d at %H:%M:%S")
        logs.write("[{}] {} was moved to {} inside a folder\n".format(time, file, new_folder))

def move_photo(file):
    new_folder = folder_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    make_logs(file, new_folder)   
    shutil.move(file, new_folder + '/' + file)

def organize():
    photos = [
        filename for filename in os.listdir('.')
        if os.path.isfile(filename) and any(filename.lower().endswith('.' + ext.lower()) for ext in extensions)
    ]
    for filename in photos:
        move_photo(filename)

organize()

