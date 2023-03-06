import sys

n = int(sys.stdin.readline())


def factorial(n):
    if n == 1:
        return 1
    
    return n*factorial(n-1)

"""
1! = 1 * 0!, 1팩토리얼이 1이기 때문에
0!은 1이 돼야 한다
"""
if n == 0:  
    print(1)
else:
    print(factorial(n))