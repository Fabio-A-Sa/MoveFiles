import os
import glob
import shutil

def search (main_directory, extensions, copy):

    # Function that search all files inside folders in current directory. Create a list with subdirectories.
    # Besides that, if copy is available, make a copy of all found files and take them to main directory. Otherwise, just transfer them.

    all_directories = []
    for extension in extensions:
        all_directories = all_directories + glob.glob( main_directory + "/**/*.{}".format(extension), recursive = True )

    if copy:
        return copy_and_move (all_directories, main_directory)
    else:
        return move_without_copy (all_directories, main_directory)


def move_without_copy (directories, pwd):

    # A function that moves all files by recursive search.

    for file in directories:
        try:
            shutil.move(file, pwd)
        except:
            continue 

    return clean_empty_folders (pwd)


def copy_and_move (directories, pwd):

    # A function that moves all copy-files by recursive search.

    for file in directories:

        try: 
            shutil.copy(file, pwd)
        except:
            continue
    
    return clean_empty_folders (pwd)


def clean_empty_folders (pwd):

    # Function that recursively cleans all empty folders after transferring files to the main directory

    folders = sorted(list(os.walk(pwd))[1:], reverse = True)
    for folder in folders:

        try:
            os.rmdir(folder[0])
            continue

        except OSError as error: 
            print("Directory '{}' can not be removed".format(folder[0])) 
            continue

