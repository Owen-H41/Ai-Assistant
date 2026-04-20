import os

def get_files_info(working_directory, directory="."):
    
    working_direc_abspath = os.path.abspath(working_directory)
    targ_direc = os.path.normpath(os.path.join(working_direc_abspath, directory))
    vaild_targ_direc = os.path.commonpath([working_direc_abspath, targ_direc]) == working_direc_abspath
    
    if not os.path.isdir(targ_direc):
        return f'Error: "{directory}" is not a directory'
    
    if vaild_targ_direc == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    directory_contents = os.listdir(targ_direc)
    directory_content_list = []
    for item in directory_contents:
        item_path = os.path.join(targ_direc, item)
        item_size = os.path.getsize(item_path)
        is_item_dir = os.path.isdir(item_path)
        directory_content_list.append(f"- {item}: file_size={item_size} bytes, is_dir={is_item_dir}")
    directory_content_string = "\n".join(directory_content_list)
    
    return directory_content_string
