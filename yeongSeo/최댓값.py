import sys

lst = []

for i in range(9):
    tmp = int(sys.stdin.readline())
    lst.append(tmp)

print(max(lst))
print(lst.index(max(lst)) + 1)