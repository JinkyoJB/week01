import sys
import itertools
from statistics import *

input = sys.stdin.readline

n = int(input()) #4
k = int(input()) #2
num_list = [str(input()).rstrip() for i in range(n)]  # ['1', '2', '12', '1']

combinations = set()
for selected in itertools.permutations(num_list, k):
    number = "".join(selected)
    combinations.add(number)

print(len(combinations))
