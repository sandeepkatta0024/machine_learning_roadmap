# 16. Merge two sorted lists
# Input
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# Expected output
# [1, 2, 3, 4, 5, 6, 7, 8]

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

list3=sorted(list1+list2)
print(list3)



# import heapq

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]

# merged = list(heapq.merge(list1, list2))
# print(merged)
