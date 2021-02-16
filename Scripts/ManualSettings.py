def settings ():

    # Input manually all extensions and copy settings

    extensions = []
    key = "Y"
    while (key != "N"):
        extension = str(input("Enter a extension to search and organize: ")).strip().replace(".", "").lower()
        extensions.append(extension)
        key = str(input("Continue? Y/N: ")).strip().upper() 

    answer = str(input("Would you like to copy all files? Yes/No: "))
    available_copy = True if answer.strip().lower() == "yes" else False
    answer = str(input("Would you like to search recursively? Yes/No: "))
    recursiveSearch = True if answer.strip().lower() == "yes" else False
    
    return extensions, available_copy, recursiveSearch
