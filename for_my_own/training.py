import re

text = "A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern. RegEx can find specific words or numbers in text that matches the pattern. Example: Jane wakes up at 8:30 every morning. RegEx pattern to find numbers in text is a sequence word or equivalent [0-9]"

''' output Upper Letter - words, numbers'''

'''
def properOut(text):
    patterns = r'([A-Z]+)([a-z]+$)'

    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
'''

print(re.findall('[A-Z][a-z]*', text))
print(re.findall('[0-9]+', text))

'''print(properOut(text))'''