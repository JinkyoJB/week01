import sys

n = int(sys.stdin.readline())

print((2 ** n) -1)

def hanoi(discs, first, middle, last):
        if discs == 0:
            return
            
        hanoi(discs - 1, first, last ,middle)

        print(first, last)

        hanoi(discs - 1, middle, first, last)

if n <= 20:
    hanoi(n, 1 , 2 ,3)

"""
n이 20이 넘어가면 연산이 2^20승, 백만회를 넘어가기에,
식으로 이동횟수를 구해줘야 함

1, 2, 3의 장대가 있고, n개의 원판을 1에서 3으로 옮기기 위해서는
1에서 2로 n-1개의 원판을 옮기고,
1에서 3으로 1개의 원판(가장큰)을 옮기고,
2에서 3으로 n-1개의 원판을 옮겨야 한다.

따라서 이때의 원판 이동횟수 T(n)은
T(n) = 2T(n-1) + 1 이고, T(1) = 1이다.

점화식을 일반항으로 옮길 수 있다

T(n) 
 = 2T(n-1) + 1
 = 2^2T(n-2) + 2 + 1 
 = 2^3T(n-3) + 2^2 + 2 + 1
 .
 .
 .
 = 2^n-1 + 2^n-2 + ... + 2 + 1 

이는 초항이 1, 공비가 2인, 항의 개수가 n인 등비수열의 합과 같으므로 
결론적으로 2^n - 1 이다.
해당 식으로 이동횟수를 구하고,
n이 20이하인 경우에는 위의 함수를 통해서 이동과정을 보여준다
"""
