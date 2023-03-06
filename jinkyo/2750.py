import sys 

input=sys.stdin.readline

a = int(input()) #5 
a_list = [int(input()) for i in range(a)]  # [5, 2, 3, 4, 1]

a_list = sorted(a_list)
for i in a_list:
    print(i)