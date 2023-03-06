import sys
from itertools import permutations

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

ops = sys.stdin.readline().strip().split()

dic = {}
dic["p"] = ops[0]
dic["m"] = ops[1]
dic["x"] = ops[2]
dic["d"] = ops[3]

op_list = []

for i in dic:
    for j in range(int(dic[i])):
        op_list.append(i)

possibles = list(permutations(op_list))
minVal = sys.maxsize
maxVal = -sys.maxsize -1

for arr in possibles:
    front = nums[0]
    res = 0
    for j in range(len(nums)-1):
        if arr[j] == "p":
            front = front + nums[j+1]

        elif arr[j] == "m":
            front = front - nums[j+1]

        elif arr[j] == "x":
            front = front * nums[j+1]

        else: # 나눗셈
            if front < 0 and nums[j+1] >0:
                front = -(-front // nums[j+1])
            else:
                front = front // nums[j+1]

    minVal = min(minVal, front)
    maxVal = max(maxVal, front)

print(maxVal)
print(minVal)
    
    
