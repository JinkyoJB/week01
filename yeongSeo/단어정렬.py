import sys

# 1. 짧은것부터
# 2. 길이 같으면 사전순
# 중복된 단어는 하나만 남기고 제거

n = int(sys.stdin.readline())

words = list(set([sys.stdin.readline().rstrip() for _ in range(n)]))

words.sort(key = lambda x:(len(x),x))

for i in words:
    print(i)