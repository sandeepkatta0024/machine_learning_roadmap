# 13. Fibonacci generator
# Generate the first 10 Fibonacci numbers.
# Input

# n = 10
# Expected output
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

n = 10
l = [0, 1]

for i in range(2, n):
    l.append(l[-1] + l[-2])

print(l)