import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

value = a*b*c

for i in range(10):
    print(str(value).count(str(i)))

