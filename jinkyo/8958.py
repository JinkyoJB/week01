import sys 

input=sys.stdin.readline

n = int(input())
arr = [input().rstrip() for i in range(n)] #['OOXXOXXOOO', 'OOXXOOXXOO', 'OXOXOXOXOXOXOX', 'OOOOOOOOOO', 'OOOOXOOOOXOOOOX']

# test1 = 'OOXXOXXOOO'
# test2= 'XXXXXXXXXX'
point=0
result = 0

for a in arr:
    for i in a:
        if i == 'O':
            point+=1
            result+=point    
        else:
            point=0
    print(result)
    point=0
    result = 0

