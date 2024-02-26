import re
def text_match(text):
        patterns = r'([A-Z]+)([a-z]+$)'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabcbbbc"))
print(text_match("Abbbc"))
print(text_match("AaabA"))

