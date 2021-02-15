import os
import glob
import shutil

def search (main_directory, extensions, copy):

    # Function that search all files inside folders in current directory. Create a list with subdirectories.
    # Besides that, if copy is available, make a copy of all found files and take them to main directory. Otherwise, just transfer them.

    all_directories = []
    for extension in extensions:
        all_directories = all_directories + glob.glob(main_directory + "/**/*.{}".format(extension), recursive = True)

    if copy:
        return copy_and_move (all_directories, main_directory)
    else:
        return move_without_copy (all_directories, main_directory)


def move_without_copy (directories, pwd):

    for file in directories:
        shutil.move(file, pwd) 

    clean_empty_folders()


def copy_and_move (directories, pwd):

    for file in directories:
        shutil.move(file, pwd)
    # Add copy!!!
    clean_empty_folders()


def clean_empty_folders ():

    # Function that recursively clears all empty folders after transferring files to the main directory

    if len(os.listdir(folder_path)) == 0: # Check if the folder is empty
        shutil.rmtree(folder_path) # If so, delete it

print([x[0] for x in os.walk(os.getcwd() )])
