import sys
from functools import *

a, b = sys.stdin.readline().split()

a_raw = list(map(int, a))
b_raw = list(map(int, b))

a_rev = []
b_rev = []

for i in range (len(a_raw)-1, -1, -1):
    a_rev.append(a_raw[i])

for i in range (len(b_raw)-1, -1, -1):
    b_rev.append(b_raw[i])

# int
a_rev_value = reduce(lambda x, y: 10*x + y, a_rev, 0)
b_rev_value = reduce(lambda x, y: 10*x + y, b_rev, 0)

print(max(a_rev_value, b_rev_value))


# list()는 str 포멧 데이터를 쪼깸. 