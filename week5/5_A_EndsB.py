import re
def text_match(text):
        patterns = r'([Aa]*)([b]+)'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aaggcfcgfbbbb"))
print(text_match("Aasdasd"))
print(text_match("Aaab"))