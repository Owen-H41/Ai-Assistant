import os

def get_file_content(working_directory, file_path):

    working_direc_abspath = os.path.abspath(working_directory)
    targ_file = os.path.normpath(os.path.join(working_direc_abspath, file_path))
    vaild_targ_file = os.path.commonpath([working_direc_abspath, targ_file]) == working_direc_abspath

    if vaild_targ_file == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(targ_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    MAX_CHARS = 10000
    with open(targ_file, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(1):
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    return file_content_string