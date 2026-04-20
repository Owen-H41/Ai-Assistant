from functions.get_files_info import get_files_info

test_cases = [
    ["calculator", "."],
    ["calculator", "pkg"],
    ["calculator", "/bin"],
    ["calculator", "../"]
]

for test_case in test_cases:
    result_string = get_files_info(test_case[0], test_case[1])
    if test_case[1] == ".":
        print(f"Result for current directory:\n{result_string}")
    else:
        print(f"Result for {test_case[1]} directory:\n{result_string}")
