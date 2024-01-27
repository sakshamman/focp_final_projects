import sys

op = sys.argv[1]
values = sys.arg[2:]

def mysum(*nums):
    s = 0
    for i in nums:
        s = s + float(i) 
    return s

def myprod(*nums):
    p = 1 
    for i in nums:
        p = p * i
    return p

if op == "s":
    ans = mysum(values)
elif op == "p":
    ans = myprod(values)
else:
    ans = "Invalid Input!"

print(ans)