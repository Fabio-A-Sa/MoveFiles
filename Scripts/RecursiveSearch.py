import glob
import shutil

def search (main_directory, extensions, copy):

    #test = ["png", "jpg"]
    #all_directories = []
    #for extension in test:
    all_directories = glob.glob(main_directory + "/**/*.png", recursive = True)
    #    all_directories.append(current_directory)

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

    #Make a disaster!
    return None
