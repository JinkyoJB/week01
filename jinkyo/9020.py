import sys
input = sys.stdin.readline

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    return True


for _ in range(int(input())):
    n = int(input())

    for i in range(n//2, -1, -1):
        if isPrime(i) and isPrime(n-i):
            print(i, n-i)
            break

# a = int(input())
# mid = a//2


# def classify(a):
#     if a == 2:
#         return 1
#     else:
#         for i in range(2, a):
#             if a % i == 0:
#                 break
#             if i == a-1:
#                 return 1
#         return 0


# while True:
#     if classify(mid) == 1 and classify(a-mid):
#         print(mid, a-mid, end=' ')
#         break
#     else:
#         mid = mid-1




