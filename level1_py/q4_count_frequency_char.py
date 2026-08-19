#Count frequency of each character in a string.
a="sandeep chowdary katta"
b={}
c=list(a)
for i in range(len(c)):
    ch=c[i]
    if ch not in b:
        b[ch]=1
        for j in range(i+1, len(c)):
            if c[j]==ch:
                b[ch]+=1

print(b)


#a = "sandeep chowdary katta"
# b = {}

# for ch in a:
#     b[ch] = b.get(ch, 0) + 1

# print(b)

