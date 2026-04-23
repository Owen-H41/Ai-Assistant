import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    if not file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file'
    
    working_direc_abspath = os.path.abspath(working_directory)
    targ_file = os.path.normpath(os.path.join(working_direc_abspath, file_path))
    vaild_targ_file = os.path.commonpath([working_direc_abspath, targ_file]) == working_direc_abspath

    if vaild_targ_file == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(targ_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    try:
        command = ["python", targ_file]
        if args != None:
            command.extend(args)

        subprocess_result = subprocess.run(command, cwd=working_direc_abspath, capture_output=True, text=True, timeout=30)
    
        result = []
        if subprocess_result.returncode != 0:
            result.append(f"Process exited with code {subprocess_result.returncode}")
        if subprocess_result.stdout == "" and subprocess_result.stderr == "":
            result.append("No output produced")
        else:
            if subprocess_result.stdout != "":
                result.append(f"STDOUT: {subprocess_result.stdout}")
            if subprocess_result.stderr != "":
                result.append(f"STDERR: {subprocess_result.stderr}")
        final_result = "\n".join(result)

        return final_result

    except Exception as e:
        return f"Error: executing Python file: {e}"