# specify the file path and keyword to search for
file_path = "/Users/mohamed-elbadri/Desktop/TestPython/palindrome.py"
keyword = "input"

# open the file and read its contents
with open(file_path, "r") as file:
    # loop through each line in the file
    for line_num, line in enumerate(file, start=1):
        # check if the keyword is in the line
        if keyword in line:
            # print the line number and content of the matching line
            print(f"Line {line_num}: {line}")

