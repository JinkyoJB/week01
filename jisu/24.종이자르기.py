import sys

h1, h2 = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())

# 초기화
# h1 = 10 가로
# h2 = 8  세로

row_input = [0, h1]
col_input = [0, h2]

row_sub = []
col_sub = []

for i in range(0, N, 1):
    # input 받기 (a= 가로/세로, b= 자르는 지점)
    a, b = list(map(int, sys.stdin.readline().split()))

    if a == 1:
        row_input.append(b)
    if a == 0:
        col_input.append(b)
    
row_input.sort()
col_input.sort()


# row, col 길이 조각들
for i in range(len(row_input)-1, 0, -1):
    sub = row_input[i] - row_input[i-1]
    row_sub.append(sub)

for i in range(len(col_input)-1, 0, -1):
    sub = col_input[i] - col_input[i-1]
    col_sub.append(sub)


# max끼리 곱
print(max(row_sub) * max(col_sub))



# case가 새로 들어올 때마다 변수를 추가해서 max(a, b1, b2, b3...)할 수는 없는 노릇.
# sort()로 매번 append되는 리스트 자체를 정렬해버리면 됨. 
# sort된 리스트에서, 왼쪽부터 차를 구해가도 됨. row[i+1] - row[i]. 



# <모범답안> 인풋 위치 굿. 
# r, c = map(int, input().split())
# # 자르는 위치
# row = [0, r]
# col = [0, c]

# for _ in range(int(input())):   # 자르는 횟수 입력
#     r_or_c, linenumber = map(int, input().split())   # 가로/세로(0 or 1), 몇줄인지로 받음
#     if r_or_c == 1:
#         row.append(linenumber)
#     else:
#         col.append(linenumber)

# row.sort()
# col.sort()

# subtracted_r = []
# subtracted_c = []

# for i in range(len(row)-1):
#     subtracted_r.append(row[i+1] - row[i])
# for i in range(len(col)-1):
#     subtracted_c.append(col[i+1] - col[i])

# print(max(subtracted_r) * max(subtracted_c))