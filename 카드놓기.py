# import sys

# n = int(sys.stdin.readline()) # 전체 카드의 수
# k = int(sys.stdin.readline()) # 합칠 카드의 수

# numbers = [sys.stdin.readline().rstrip() for i in range(n)]

# array = set()

numbers = ["1", "2", "3", "4", "5"]
array = set()
visit = [0] * 5
k = 2

""" itertools permutation 라이브러리 존재함 """
def permutation(count, perm, visit):
    global numbers
    if count == k:
        array.add(''.join(perm))
        return
    for idx in range(5):
        if not visit[idx]:
            visit[idx] = 1
            permutation(count + 1, perm+[numbers[idx]], visit)
            visit[idx] = 0

# visit = [0] * n
# permutation(0, [], visit)
# print(len(array))

permutation(0, [], visit)