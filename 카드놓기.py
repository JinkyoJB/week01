
""" 
1. itertools활용하여 순열로 푼 풀이
"""
# import sys
# from itertools import permutations

# input = sys.stdin.readline

# n = int(input())
# k = int(input())

# cards = [input().rstrip() for _ in range(n)]

# cases = set(map(lambda x:''.join(x) ,permutations(cards, k)))

# print(cases)

# print(len(cases))


"""
2. 재귀로 이어붙인 풀이 
"""
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

cards = [input().rstrip() for _ in range(n)]

dp = [0] * n
res = set()

def concat(cards, curStr ,count):

    if (count == k):
        res.add(''.join(curStr))
        return
    
    for i in range(n):
        if dp[i] == 0:
            dp[i] = 1
        
            concat(cards, curStr + [cards[i]] ,count + 1)

            dp[i] = 0


concat(cards, [] ,0)
print(len(res))
        
        

