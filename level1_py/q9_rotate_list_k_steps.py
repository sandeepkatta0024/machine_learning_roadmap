# 9. Rotate a list by k steps
# Input
# nums = [1, 2, 3, 4, 5]
# k = 2
# Expected output
# [4, 5, 1, 2, 3]
# Assume rotation is to the right.


k = 2
nums = [1, 2, 3, 4, 5]

nums= nums[-k:]+nums[:-k]
#The Cheat Sheet to Memorize
# Slice	Meaning	On [1,2,3,4,5]
# nums[2:]	from index 2 to end	[3, 4, 5]
# nums[:2]	from start up to (not including) index 2	[1, 2]
# nums[-2:]	last 2 elements	[4, 5]
# nums[:-2]	everything except last 2 elements	[1, 2, 3]
# nums[::-1]	reverse the whole list	[5, 4, 3, 2, 1]
# nums[1:4]	index 1 up to (not incl.) index 4	[2, 3, 4]
print(nums)