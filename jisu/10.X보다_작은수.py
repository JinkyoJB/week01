N, X = input().split()
A = input().split()

N = int(N)
X = int(X)
A = list(map(int, A))

for i in range(0, N, 1):
    if A[i] < X:
        print(A[i], end = " ")


# map : split이 문자열 리스트로 가져온 것을 원하는 자료형 리스트로 변환.