A = []
for i in range(0, 9, 1):
    x = int(input())
    A.append(x)

print(max(A))

print(A.index(max(A))+1)


# input 받을 때마다 int로 변환하기


# A = []
# for i in range(0, 9, 1):
#     A.append(input())
# A = list(map(int, A))

# print(max(A))

# for index in range(0, len(A), 1):
#     if A[index] == max(A):
#         print(index)