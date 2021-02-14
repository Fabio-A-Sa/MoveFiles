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

    # Filter [extensions] by file's status in dictionary

    files = display()
    extensions = []

    for type, extensions in respective_extension.items():
        if type in files:
            for extension in extensions:
                if extension not in ext:
                    ext.append(extension)

    return extensions
