import sys, math
from itertools import permutations

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

permute = list(permutations(nums, n))

maxed = 0

for case in permute:
    computed = 0
    for i in range(n-1):
        computed += abs(case[i] - case[i+1])
    
    maxed = max(computed, maxed)

print(maxed)
