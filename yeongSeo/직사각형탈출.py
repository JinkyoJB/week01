import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

distances = [w - x, x, y, h -y]

print(min(distances))



