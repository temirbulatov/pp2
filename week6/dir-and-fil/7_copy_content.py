import os

#path "C://Users//temir//Desktop//abc"

with open(r"C://Users//temir//Desktop//abc//file1.txt", 'r') as fp:
    f = open("C://Users//temir//Desktop//abc//file2.txt", "w")
    f.write((fp.read()))
    f.close()


content = open('C://Users//temir//Desktop//abc//file2.txt')
print(content.read())