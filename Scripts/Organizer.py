
# Import modules

import extensions
import os
import shutil
from datetime import datetime
from PIL import Image

DATETIME_EXIF_INFO_ID = 36867

def folder_path_from_photo_date(file):
    date = photo_shooting_date(file)
    return date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')

def photo_shooting_date(file):

    date = "nothing"
    photo = Image.open(file)

    if hasattr(photo, '_getexif'):
        info = photo._getexif()
        print(info)
        if info:
            if DATETIME_EXIF_INFO_ID in info.keys():
                date = info[DATETIME_EXIF_INFO_ID]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')

    if type(date) == str:
        date = datetime.fromtimestamp(os.path.getmtime(file))

    return date

def make_log (file, new_folder):

    now = datetime.now()
    cwd = os.getcwd()
    time = now.strftime("%Y-%m-%d at %H:%M:%S")
    
    with open("Logs.txt", "a") as logs:

        logs.write(' [{}]        " {} "   was moved to folder   "{}"   inside of   "{}"\n'
                   .format(time, file, new_folder[5:], new_folder[:4]))
        logs.write('Current directory: {}\{}\{}\n'.format(cwd, new_folder[:4], new_folder[5:]))
        logs.write(" \n")


def move_photo(file):
    new_folder = folder_path_from_photo_date(file)
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    make_log (file, new_folder)   
    shutil.move(file, new_folder + '/' + file)

def organize():
    enable_extensions = extensions.enable_extensions()
    photos = [
        filename for filename in os.listdir('.')
        if os.path.isfile(filename) and any(filename.lower().endswith('.' + ext.lower()) for ext in enable_extensions.keys())
    ]
    for filename in photos:
        move_photo(filename)

organize()



