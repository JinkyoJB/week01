import sys

heights = [int(sys.stdin.readline()) for _ in range(9)]

heights_set = set(heights)

total = sum(heights)

for i in range(9):
    complement = total - heights[i] - 100

    # 자기가 자신의 complement가 되는 경우는 제해줘야 함
    if complement in heights_set and complement != heights[i]:
        heights_set.remove(complement)
        heights_set.remove(heights[i])
        break

heights = list(heights_set)
heights.sort()
for i in heights:
    print(i)



