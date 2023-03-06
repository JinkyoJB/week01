
"""
메모리제한 : 8MB = 800만 byte 
sizeof(int[1~10000]) : 28byte
주어지는 수의 개수가 최대 10,000,000 개 이므로,
리스트에 이를 담을 시 메모리를 초과한다

값의 범위가 1~10000임을 이용하여 10000칸을 가진 배열 생성하고,
배열의 인덱스를 기준으로 들어오는 값의 개수를 기록
"""
import sys
# a = 10000
# print(sys.getsizeof(a))

n = int(sys.stdin.readline())

nums = [0] * 10001

for i in range(n):
    tmp = int(sys.stdin.readline())
    nums[tmp] += 1

for i in range(1, 10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)