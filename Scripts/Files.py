# Change and add file status if you need

available_files =   {

                    "photos": "enabled", 
                    "text" : "disabled",  
                    "web" : "enabled",      
                    "code" : "enabled",    
                    
                    }

def display () :

    # Filter files by type/status in dictionary

    all_files = [file for file,status in available_files.items() if status == "enabled"]
    return all_files

