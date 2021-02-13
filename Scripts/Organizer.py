
# Import modules

import extensions
import os
import shutil
from datetime import datetime
from PIL import Image

"""
{36864: b'0210', 
 37121: b'\x01\x02\x03\x00', 
 37377: 7.149, 
 36867: '2020:10:18 12:33:53', 
 36868: '2020:10:18 12:33:53', 
 37378: 2.27, 
 37379: 0.0, 
 37380: 0.0, 
 37383: 2, 
 37384: 0, 
 37385: 0, 
 37386: 3.46, 
 40961: 1, 
 40962: 3120, 
 40965: 850, 
 41991: 0, 
 37520: '951268', 
 37521: '951268', 
 37522: '951268', 
 40963: 4160, 
 41996: 0, 
 257: 4160, 
 258: (8, 8, 8), 
 41495: 2, 
 271: 'HUAWEI', 
 41728: b'\x03', 
 33434: 0.007029658, 
 282: 72.0, 
 531: 1, 
 33437: 2.2, 
 41729: b'\x01', 
 283: 72.0, 
 42016: '7e9f6d2e276f26290000000000000000', 
 34850: 2, 
 41985: 1, 
 34855: 100, 
 296: 2, 
 41986: 0, 
 40960: b'0100', 
 256: 3120, 
 41987: 0, 
 305: 'ATU-L21 8.0.0.151(C33)', 
 306: '2020:10:18 12:33:53', 
 41989: 26, 
 41992: 0, 
 41993: 0, 
 41994: 0, 
 272: 'ATU-L21', 
 34665: 250, 
 530: (2, 2)}
"""
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



