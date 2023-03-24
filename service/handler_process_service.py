from utility import handler_process_utils

def split_fullname(fullname):
    if fullname == "":
        handler_process_utils.raise_error("Variable name is empty")
    else:
        try:
            name_list = fullname.split()
            if len(name_list) == 1:
                handler_process_utils.handle_error("User has no surname")
                return name_list[0], "", ""
            if len(name_list) > 2:
                return name_list[0], name_list[1], name_list[2]
            else:
                return name_list[0], name_list[1], ""
        except:
            handler_process_utils.raise_error("Problem getting out user name and surnname")