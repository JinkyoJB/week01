import sys

input = sys.stdin.readline

a = input().strip()
if a=='':
    print(0)
else:
    print(a.count(' ')+1)
