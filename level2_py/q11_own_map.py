# Input
# nums = [1, 2, 3, 4, 5]

# function = square
# Where conceptually:
# square(x) → x * x
# Expected output
# [1, 4, 9, 16, 25]

def map(nums):
    l=[]
    for i in nums:
        l.append(i*i)
        
    
    return l


nums = [1, 2, 3, 4, 5]
print(map(nums))

