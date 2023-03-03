import sys

n = int(sys.stdin.readline())

def queens(n):
    if n == 1:
        return n ** 2

    return n**2 - queens(n-1) 

print(queens(8))