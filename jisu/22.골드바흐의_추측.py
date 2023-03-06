import sys

T = int(sys.stdin.readline())

def sosu(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


for i in range(0, T, 1):
    num = int(sys.stdin.readline())
    half = int(num / 2)

    if num == 4:
        a = 2
        b = 2

    elif half % 2 == 0:
        a = half - 1
        b = half + 1

    else:
        a = half
        b = half 

    # 소수 확인
    while sosu(a) == False or sosu(b) == False:
        a -= 2
        b += 2

    print(a, b)


# 각 케이스가 한 줄 씩 받을경우 for문 안에 input을 넣는다. 
# 나누기는 항상 int()를 염두. for문 range( )에는 float가 들어갈 수 없다. 