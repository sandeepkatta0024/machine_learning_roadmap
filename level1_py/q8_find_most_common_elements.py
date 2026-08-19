# 8. Find common elements in two lists
# Input
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Expected output
# [3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list1.sort()
list2.sort()
common_list=[]
for i in list1:
    for j in list2:
       if i==j:
            common_list.append(i)
print(common_list)





# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common_list = list(set(list1) & set(list2))
# print(common_list)