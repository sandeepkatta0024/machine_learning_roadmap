# 10. Check if a number is a palindrome
# Input
# num = 1221
# Expected output
# True
# Another:
# num = 1234
# Expected:
# False

def checkPalindrome(num1):
    l=list(str(num1))
    l=l[::-1]
    l="".join(l)
    return num1==int(l)


if checkPalindrome(121):
    print("Yes its Palindrome")
else:
    print("No!! its not a Palindrome")
