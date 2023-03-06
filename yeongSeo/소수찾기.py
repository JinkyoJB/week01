import sys, math

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))

count = 0
for i in lst:
    if i == 1:
        continue

    isPrime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            isPrime = False
            break

    if isPrime == True:
        count += 1

print(count)