#Check if two strings are anagrams.
def check_anagrams(a,b):
    a="".join(sorted(a))
    b="".join(sorted(b))


    return a==b

a="sandeep"
b="act"
c="cat"

print(check_anagrams(c,b))

