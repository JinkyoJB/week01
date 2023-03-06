n = int(input())

def move(no:int, x:int, y:int):
    if no>20:
        return
    if no>1:
        move(no-1, x, 6-x-y)
    
    print(x, y, sep=' ')

    if no>1:
        move(no-1, 6-x-y, y)


print(2**n - 1)
move(n, 1, 3)
