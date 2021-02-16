# Modules

import RecursiveSearch
import Extensions
import Files
import os
import shutil
from datetime import datetime
from PIL import Image
from time import sleep, perf_counter

# Functions

def make_new_directory (file):

    # Function that makes a folder name, based on exif data, 
    # and a new directory inside a main year

    date = extract_date (file)
    new_directory = date.strftime('%Y') + '/' + date.strftime('%Y-%m-%d')
    
    return new_directory


def extract_date (file):

    # Function that extracts files' date using exif and Pillow module.
    # Converts in future folder-structure date

    date = "unknown"
    photo = Image.open(file)

    if hasattr(photo, '_getexif'):
        # If it is possible to extract exit data
        
        info = photo._getexif()
        date_id = 36867
        
        if info != None:
            # If exif contains data to search

            if date_id in info.keys():
                date = info[date_id]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')

    if date == "unknown":
        # Date has not changed, use the modified date by os.path.getmtime
        date = datetime.fromtimestamp(os.path.getmtime(file))

    return date


def make_log (file, new_folder):

    now = datetime.now()
    # After move file, gets a new directory
    pwd = os.getcwd() 
    time = now.strftime("%Y-%m-%d at %H:%M:%S")
    
    with open("Logs.txt", "a") as logs:
        # Append mode. Add new data to the end of the file, new log is automatically amended.

        logs.write('[{}]   " {} "   was moved to folder   "{}"   inside of   "{}"\n'
                   .format(time, file, new_folder[5:], new_folder[:4]))
        
        logs.write('Current directory: {}\{}\{}\n'.format(pwd, new_folder[:4], new_folder[5:]))
        logs.write(" \n")


def move (file):
    
    new_folder = make_new_directory (file)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
        
    make_log (file, new_folder)   
    shutil.move(file, new_folder + '/' + file)


def organize (recursive_search, extensions, copy):

    # Current directory
    pwd = os.getcwd() 

    if recursive_search:
        RecursiveSearch.search(pwd, extensions, copy)
    
    # All files ending possible in extensions
    files = [
                filename 
                for filename in os.listdir('.')
                if os.path.isfile(filename) and 
                any(filename.lower().endswith('.' + ext.lower()) for ext in extensions)
            ]

    moves = 0
    t0 = perf_counter()

    for file in files:
        move (file)
        moves += 1

    t1 = perf_counter()
    time = round(t1 - t0, 2)

    print('Success. {} files were moved and organized in {} seconds.'.format(moves, time))


recursiveSearch = True
copy = False
extensions = Extensions.make_extensions()

organize (recursiveSearch, extensions, copy)
