# 7. Flatten a nested list
# Input
# nested = [[1, 2], [3, 4], [5, 6]]
# Expected output
# [1, 2, 3, 4, 5, 6]
# Try this afterward:
# nested = [[1, 2], [3, [4, 5]], [6]]
# Decide whether your function handles only one level or arbitrarily nested lists.

l=[]
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            l.append(item)


nested = [[1, 2], [3, [4, 5]], [6]]
flatten(nested)
print(l)
