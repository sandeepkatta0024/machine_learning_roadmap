# 12. Implement your own filter()
# Input
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# Filter condition:
# keep numbers divisible by 2
# Expected output
# [2, 4, 6, 8]

def filter(x):

    l=[]
    for i in x:
        if i %2==0:
            l.append(i)
    return l

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(filter(nums))
