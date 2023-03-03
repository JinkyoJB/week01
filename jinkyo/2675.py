import sys 

input=sys.stdin.readline

n = int(input())
data = [input().split() for _ in range(n)] #[['3', 'ABC'], ['5', '/HTP']]



for t in data:
    for i in t[1]:
        for a in i:
            print(a*int(t[0]),end='')
    print()