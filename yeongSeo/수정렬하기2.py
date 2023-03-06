import sys, heapq

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]

heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))