import sys

ab = [sys.stdin.readline() for i in range(2)]
a = int(ab[0])
b = int(ab[1])

print(a * (b % 10))
print(a * ((b // 10) % 10))
print(a * (b // 100))
print(a*b)