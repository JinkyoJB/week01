import sys

t = int(sys.stdin.readline())

lst = []
for i in range(t):
    a, b= map(int, sys.stdin.readline().strip().split())
    lst.append(a+b)

for i in lst:
    print(i)