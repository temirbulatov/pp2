#'C://Users//temir//Desktop//abc'

#create files with letters

import string, os
if not os.path.exists("C://Users//temir//Desktop//abc"):
   os.makedirs("C://Users//temir//Desktop//abc")
for letter in string.ascii_uppercase:
   with open("C://Users//temir//Desktop//abc//"+ letter + ".txt", "w") as f:
       f.writelines(letter)