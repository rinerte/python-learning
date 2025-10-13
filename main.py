# files
import os

# # path = "C:\\Users\\paand\\Documents\\example.txt"
# path = "C:\\Users\\paand\\Documents"

# if os.path.exists(path):
#     print("Location exists.")
#     if os.path.isfile(path):
#         print("It's a file.")
#     elif os.path.isdir(path):
#         print("It's a directory.")
# else:
#     print("File does not exist.")

# # Reading a file
# try:
#     with open("tes.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")

# text = "This is a test file.\nThis is the second line."

# with open("test2.txt", "w") as file:
#     file.write(text)


# copyfile() = copies contents of a file
# copy() = copies file and permission mode + destination can be a directory
# copy2() = copies file, permission mode, and metadata (like creation and modification times)

# import shutil

# shutil.copyfile("test2.txt", "test3.txt")
# shutil.copy("test2.txt", "C:\\Users\\paand\\Documents")
# shutil.copy2("test2.txt", "test4.txt")


# MOVING FILES

import os

source = "test.txt"
destination = "C:\\Users\\paand\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("File already exists at destination.")
    else:
        os.replace(source, destination)
        print(f"Moved file from {source} to {destination}.")

except FileNotFoundError as e:
    print(e)
    print("Source file not found.")

