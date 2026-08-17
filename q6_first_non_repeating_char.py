# 6. Find the first non-repeating character
# Input
# s = "aabbcdeeff"
# Expected output
# c


s= "aabbcdeeff"
res=''
for i in range(len(s)):
    ch = s[i]
    repeat=False
    for j in range(len(s)-1):
        if i!=j and s[i]==s[j]:
            repeat=True
            break

    if not repeat:
        print(ch)
        break
