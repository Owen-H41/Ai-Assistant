import os

def write_file(working_directory, file_path, content):

    working_direc_abspath = os.path.abspath(working_directory)
    targ_file = os.path.normpath(os.path.join(working_direc_abspath, file_path))
    vaild_targ_file = os.path.commonpath([working_direc_abspath, targ_file]) == working_direc_abspath

    if vaild_targ_file == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if  os.path.isdir(targ_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    try:
        parent_direc = os.path.dirname(targ_file)
        os.makedirs(parent_direc, exist_ok=True)
    except Exception as e:
        print(f"Error:{e}")

    with open(targ_file, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'