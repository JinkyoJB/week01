import sys 

input=sys.stdin.readline

a,b,v= map(int, input().split())

high = v-a
day_length=a-b
if high % (a-b) == 0:
    print(high//day_length+1)
else:
    print(high//day_length+2)
