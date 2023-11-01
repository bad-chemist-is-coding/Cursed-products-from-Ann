# with open("demo24_my_file.txt") as file: # Read only mode: mode = "r"
#     # file = open("demo24_my_file.txt")
#     contents = file.read()
#     print(contents)
#     # file.close()

# mode:
# r = read
# w = write
# a = append

with open("demo24_my_file.txt", mode="a") as file:
    file.write("\nBye World")

with open("demo24_new_file.txt", mode="w") as file:  # open new file will auto create a new file (only in write mode)
    file.write("\n No to world")

# Absolute File Path: path start from root = /big_folder/folder/file.x
# Relative File Path: ./folder/file.x (Reverse path: using ../ instead of ./)
# ex: demo24_new_file.txt is in the desktop
# => with open("/User/.../Desktop/demo24_my_file.txt") as file:
# Jump back to folder => with open("../../Desktop/demo24_my_file.txt") as file:
