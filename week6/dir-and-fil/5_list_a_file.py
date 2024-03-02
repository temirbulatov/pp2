import os

lst = ['Steam', 'Witcher']
with open('C://Users//temir//Desktop//abc.txt', "w") as myfile:
        for c in lst:
                myfile.write("%s\n" % c)

content = open('C://Users//temir//Desktop//abc.txt')
print(content.read())