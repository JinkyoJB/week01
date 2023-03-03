import sys

input=sys.stdin.readline

a = int(input())
mid = a//2

def classify(a):
    if a==2:
        return 1
    else:
        for i in range(2,a):
            if a%i==0:
                break
            if  i==a-1:
                return 1
        return 0

while True:
    if classify(mid)==1 and classify(a-mid):
        print(mid, a-mid, end=' ')
        break
    else:
        mid=mid-1



