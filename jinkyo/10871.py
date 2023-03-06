import sys 

input=sys.stdin.readline

n, x = map(int, input().split())

arr = list(map(int, input().split()))

# print(a,b, arr) # 10 5 [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]
for i in range(n):
    if arr[i] < x:
        print(arr[i], end=" ")



