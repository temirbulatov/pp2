#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(word):
    cleaned = ''
    for char in word:
        if char.isalnum():
            cleaned += char.lower()
    reversed_word = cleaned[::-1]
    return cleaned == reversed_word

input_word = input("Enter smth: ")
result = is_palindrome(input_word)

if result:
    print(f"{input_word} is palindrome.")
else:
    print(f"{input_word} is not palindrome.")