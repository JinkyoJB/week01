import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(n)]


def divide(arr):
    if len(arr) == 1:
        return arr
    
    return merge(divide(arr[:len(arr)//2]), divide(arr[len(arr)//2:]))


def merge(arr1, arr2):
    res = []

    idx1 = 0
    idx2 = 0

    while (idx1 < len(arr1) and idx2 < len(arr2)):
        if arr1[idx1] >= arr2[idx2]:
            res.append(arr2[idx2])
            idx2 += 1
        else:
            res.append(arr1[idx1])
            idx1 += 1
    
    if idx1 < len(arr1):
        res += arr1[idx1:]
    else:
        res += arr2[idx2:]
    
    return res

arr  = divide(arr)
for i in arr:
    print(i)