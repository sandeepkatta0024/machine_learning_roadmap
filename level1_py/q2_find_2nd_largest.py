#Find the second largest number in a list.
l=[1,10,22,33,2,33,44,55,44,55,66,77,88,77]
unique_list=list(set(l))
unique_list.sort()
print(unique_list[-2])