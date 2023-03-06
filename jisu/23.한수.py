import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(1, N+1, 1):
    if i < 100:
        cnt += 1
    else:
        x1 = i // 100
        x2 = i % 100 // 10
        x3 = i % 10

        if x1 - x2 == x2 - x3:
            cnt += 1

print(cnt)

# 뭐가 돌고 있는지 잘 확인. N이 아니라 i임. 