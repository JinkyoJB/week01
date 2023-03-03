T = int(input())

res = []

for i in range(0, T, 1):
    A, B = input().split()
    A = int(A)
    B = int(B)
    C = A + B
    res.append(C)

for i in range(0, T, 1):
    print(res[i])
