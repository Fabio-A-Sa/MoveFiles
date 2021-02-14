# Add extensions or modify extensions status if you need

extensions =    {

                "jpg" : "enabled" ,
                'png' : "enabled" ,
                'jpeg': "enabled" ,
                'txt' : "disabled" ,
                'html' : 'disabled' ,
                'css' : 'disabled' ,
                'js' : 'disabled' ,

                }

def enabled_extensions () :

    # Filter extensions by status in dictionary
    all_extensions = [ext for ext,status in extensions.items() if status == "enabled"]

    return all_extensions