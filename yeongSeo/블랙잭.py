import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

cards = list(map(int, sys.stdin.readline().split()))

combi = list(map(lambda x:sum(x), list(combinations(cards,3))))
combi.sort()

for i in range(len(combi)-1):
    if combi[i] == m or combi[i+1] > m:
        print(combi[i])
        exit(0)

print(combi[-1])
    




