def isPalindrome(s):
    return s == s[::-1]

s = "POPOP"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")