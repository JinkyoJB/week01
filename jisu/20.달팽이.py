import sys

A, B, V = sys.stdin.readline().split()
A = int(A)
B = int(B)
V = int(V)

dist = A - B

if (V - A) % dist == 0:
    days = (V - A) // dist + 1
    print(days)
else:
    days = (V - A) // dist + 2
    print(days)

# else: 최소 지점까지 한 번 더(다음날 +1), 최소지점에서 목적지까지 한 번 더(+1)


# 시간초과
# dist = 0
# days = 0

# while dist + A < V:
#     dist += (A - B)
#     days += 1

# print(days + 1)



