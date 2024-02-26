import re
text = 'ENG 1926., 260224.'
print(re.sub("[ ,.]", ":", text))