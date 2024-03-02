import os

path = "C://Users//temir//Desktop//"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")

print(dir_list)
print("\n")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\n")
print([ name for name in os.listdir(path)])