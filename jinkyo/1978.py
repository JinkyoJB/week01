import sys 

input=sys.stdin.readline

n = int(input())
arr = map(int, input().split())


count=0
for a in arr:
    if a==2:
        count+=1
    for i in range(2, a):
        if a%i == 0:
            break
        if i==a-1:
            count+=1
print(count)
