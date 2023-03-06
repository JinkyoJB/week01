# import sys

# n, r, c = map(int, sys.stdin.readline().split())
# ans = 0

# def solve(x, y, n):
#     global ans
        
#     if x == r and y == c:
#         print(ans)
#         exit(0)

#     if n == 1:
#         ans += 1
#         return
    
#     if not(x <= r < x+n and y <= c < y+n):
#         ans += n*n
#         return

#     temp = n // 2
#     solve(x, y , temp)
#     solve(x, y+temp , temp)
#     solve(x+temp, y , temp)
#     solve(x+temp, y+temp , temp)

# solve(0, 0, 2**n)


import sys

n, r, c = map(int, sys.stdin.readline().split())

count = 0

def move(n, startY, startX):
    global count

    if n == 0 and startY == r and startX == c:
        print(count)
        return
    
    if n == 0:
        count += 1
        return

    if not(startY <= r < startY+2**n and startX <= c <= startX+2**n):
        count += (2**n)**2
        return
    
    move(n-1, startY, startX)
    move(n-1, startY, startX + 2**(n-1))
    move(n-1, startY + 2**(n-1), startX)
    move(n-1, startY + 2**(n-1), startX + 2**(n-1))

move(n, 0, 0)


