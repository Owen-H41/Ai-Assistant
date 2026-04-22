from functions.get_file_content import get_file_content

test_cases = [
    ["calculator", "lorem.txt"],
    ["calculator", "main.py"],
    ["calculator", "pkg/calculator.py"],
    ["calculator", "/bin/cat"],
    ["calculator", "pkg/does_not_exist.py"]
]

for test_case in test_cases:
    text = get_file_content(test_case[0], test_case[1])
    if len(text) > 10000:
        print(len(text))
        print(text[-60:])
    else:
        print(text)
