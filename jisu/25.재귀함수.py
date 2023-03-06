import sys

N = int(sys.stdin.readline())

def factorial(n):
    if n == 1:
        res = 1
        return(res)
    res = n * factorial(n-1)
    return(res)

factorial(N)