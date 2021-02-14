import glob
import shutil

def search (main_directory, extensions):

    #test = ["png", "jpg"]
    #all_directories = []
    #for extension in test:
    current_directory = glob.glob(main_directory + "/**/*.png", recursive = True)
    #    all_directories.append(current_directory)

    return move(current_directory, main_directory)

def move (alist, pwd):
    for item in alist:
        shutil.move(item, pwd) 
