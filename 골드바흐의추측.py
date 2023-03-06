import sys, math

def isPrime(val):
    for j in range(2, int(math.sqrt(val)) + 1):
        if val % j == 0:
            return False

    return True
    

t = int(sys.stdin.readline())

evens = [int(sys.stdin.readline()) for i in range(t)]

for i in evens:
    for part in range(i//2, 1, -1):
        if isPrime(part):
            if isPrime(i - part):
                print(str(part) + " " + str(i-part))
                break

