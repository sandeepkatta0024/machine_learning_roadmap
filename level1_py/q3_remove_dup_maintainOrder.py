l=[1,10,22,33,2,33,44,55,44,55,66,77,88,77]
for i in range(len(l)):
    for j in range(len(l)-1,i,-1):
        if l[i]==l[j]:
            del l[j]

print(l)