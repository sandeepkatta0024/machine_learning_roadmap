# 20. Implement stack using queues
# Operations:
# push(10)
# push(20)
# push(30)
# pop()
# pop()
# push(40)
# pop()
# Expected output
# 30
# 20
# 40
l=[]
def push(a):
    l.append(a)
def pop():
    if l[-1] is not None:
        print(l[-1])
        l.remove(l[-1])
push(10)
push(20)
push(30)
pop()
pop()
push(40)
pop()

print(l)