import sys

abc = [int(sys.stdin.readline()) for i in range(3)]
res= str(abc[0] * abc[1] * abc[2])


for i in range(10):
    count = 0
    for j in res:
        if j == str(i):
            count += 1
    print(count)
