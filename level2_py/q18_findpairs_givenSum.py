# 18. Find all pairs with given sum
# Input
# nums = [2, 4, 3, 5, 7, 8, 9]
# target = 7
# Expected output
# [(2, 5), (4, 3)]
# Order doesn't matter.

nums = [2, 4, 3, 5, 7, 8, 9]
target = 7
result=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j]==target:
            result.append((nums[i],nums[j]))


print(result)