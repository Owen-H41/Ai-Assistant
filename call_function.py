from functions.function_schemas import *

available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)
