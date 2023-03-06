import sys 

input=sys.stdin.readline

x, y, w, h = map(int, input().split())

a = [x,y,w-x,h-y]
print(min(a))