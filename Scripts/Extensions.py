# Add extensions or modify extensions status if you need

from Files import display

respective_extension =  {

                        "photos": ['png', 'jpg', 'jpeg'] ,
                        "text" : ['txt'] ,
                        "web" : ['html', 'css', 'js'] ,
                        "code" : ['html', 'css', 'js', 'py', 'cpp'] ,

                        }   

all_extensions =    {

                    "jpg" : "enabled" ,
                    'png' : "enabled" ,
                    'jpeg': "enabled" ,
                    'txt' : "disabled" ,
                    'html' : 'disabled' ,
                    'css' : 'disabled' ,
                    'js' : 'disabled' ,
                    'py' : 'disabled' ,
                    'cpp' : 'disabled' ,

                    }

def make_extensions ():

    # Filter [extensions] by files and extensions status in dictionary

    files = display()
    all_ext = []

    for type, extensions in respective_extension.items():
        if type in files:
            for extension in extensions:
                if (extension not in all_ext) and (all_extensions[extension] == "enabled"):
                    all_ext.append(extension)

    return all_ext