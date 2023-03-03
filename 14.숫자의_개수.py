A = int(input())
B = int(input())
C = int(input())

X = A * B * C
X = list(map(int, list(str(X))))

for i in range(0, 10, 1):        # 0부터 9까지 나타날 숫자
    cnt = 0
    for j in range(0, len(X), 1):
        if X[j] == i:
            cnt += 1
    print(cnt)