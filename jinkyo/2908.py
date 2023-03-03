import sys

input = sys.stdin.readline

a,b = map(str, input().split())
c=[a[::-1],b[::-1]]

print(max(c))