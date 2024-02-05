#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection set.

def unique_elements(l):
    result = []
    for elem in l:
        if elem not in result:
            result.append(elem)
    return result

inputl = [1, 2, 2, 3, 4, 4, 5]
output = unique_elements(inputl)

print("unique elements: ", output)