import sys, math

a,b,v = map(int, sys.stdin.readline().split())

tmp = (v-a) / (a-b)
tmp = math.ceil(tmp)

print(tmp + 1)