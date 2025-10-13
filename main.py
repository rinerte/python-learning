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

text = "This is a test file.\nThis is the second line."

with open("test2.txt", "w") as file:
    file.write(text)