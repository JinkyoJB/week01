import sys

T = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

for num in arr:
    if num > 1:
        excl = 0 
        for i in range(2, num):
            if num % i == 0:
                excl += 1
        if excl == 0:
            cnt += 1
print(cnt)


# 변수 초기화의 위치. 매 수마다 판단할 거면 for문 안에 excl = 0이 있고, 전체 cnt = 0은 for 바깥에 있어야. 
# False 경우의 수가 없으면(0) True라고 판단.
# 1 예외 처리 