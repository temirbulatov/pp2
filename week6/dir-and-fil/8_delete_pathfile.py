

import os 
path = "C://Users//temir//Desktop//Songif.txt"

#path = input("Enter the path in the form C://smth//smth//smth:")
'''
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path , os.X_OK))
'''


if (os.access(path, os.F_OK)):
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path , os.X_OK))

    os.remove("C://Users//temir//Desktop//Songif.txt")
    
    if not (os.access(path, os.F_OK)):
        print("file deleted")
else:
    print('Existence of the file:', os.access(path, os.F_OK))
