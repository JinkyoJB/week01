import sys
from statistics import *

input=sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)] #[[5, 50, 50, 70, 80, 100], [7, 100, 95, 90, 80, 70, 60, 50], [3, 70, 90, 80], [3, 70, 90, 81], [9, 100, 99, 98, 97, 96, 95, 94, 93, 91]]

for a in arr:
    ave=mean(a[1:])
    num = 0
    for i in a[1:]:
        if i > ave:
            num+=1
    result = round((num/a[0])*100,3)
    print(f"{result:.3f}%")



