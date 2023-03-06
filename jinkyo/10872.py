import sys

input=sys.stdin.readline

a = int(input())

def facto(num):
    if num==0:
        return 1
    else:
        return num*facto(num-1)
    
print(facto(a))
