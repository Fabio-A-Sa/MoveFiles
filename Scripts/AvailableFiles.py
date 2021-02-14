# Change and add file status if you need

available_files =   {

                    "photos": "enabled",      # .png, .jpg, .jpeg
                    "text" : "disabled",      # .txt
                    "web" : "disabled",       # .html, .css, .js
                    "code" : "disabled",      # .html, .css, .js, .py, .cpp
                    
                    }

def display():

    # Filter avail
    availables = [type for type,status in available_files.items() if status == "enabled"]
    print(available_files)
    return availables

