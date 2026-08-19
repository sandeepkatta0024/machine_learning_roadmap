# 15. Group words that are anagrams
# Input
# words = [
#     "eat",
#     "tea",
#     "tan",
#     "ate",
#     "nat",
#     "bat"
# ]
# Expected output
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
# Order of groups doesn't matter.


words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]
l={}
for i in words:
    temp=list(i)
    temp.sort()
    temp="".join(temp)
    l[temp]=i
print(l)