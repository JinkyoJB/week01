# import sys
# n = int(sys.stdin.readline())


# def hanoi(n, from_pos, to_pos, aux_pos):
#     if n == 1:
#         print(from_pos, ' ', to_pos)
#         return

#     hanoi(n-1, from_pos, aux_pos, to_pos)
#     print(from_pos, ' ', to_pos)             
#     hanoi(n-1, aux_pos, to_pos, from_pos)

# print(2**n-1)
# hanoi(n, 1, 3, 2)


# 홀/짝 안나눠도 됨. 
# 결과값은 from, to만 있으면 되지만 
# 함수에는 A, B, C 기둥 모두 정의되어야 from, to가 아닌 다른 기둥을 표현할 수 있다.

import sys
n = int(sys.stdin.readline())


def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, ' ', to_pos)
        return 1;

    s1 = hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, ' ', to_pos)             
    s2 = hanoi(n-1, aux_pos, to_pos, from_pos)
    return s1 + s2 + 1

hanoi(n, 1, 3, 2)

# print(f"{n}번째 원반을 {from_pos}에서 {to_pos}로 이동")








# hanoi(4, A, C)  # 4개 원반을 A에서 C로 옮긴다. 출발/도착지는 정해져있음. 

# hanoi(3, A, B)  # C는 비워둘 것.

# hanoi(2, A, C) # B는 비워둘 것.

# hanoi(1, A, B) # C는 비워둘 것.



# hanoi(5, A, C)

# hanoi(4, A, B)

# hanoi(3, A, C)

# hanoi(2, A, B)

# hanoi(1, A, C)

# # 거꾸로 값을 반환하며 출력하는 형태.

# # 초기값
# def hanoi(n):
#     if n % 2 == 0:
#         hanoi(2) = print(1,2), print(1,3), print(2,3)
#     else: hanoi(2) = print(1,3), print(1,2), print(3,2)

#     if n == 짝수:
#         hanoi(1, A, B)
#     else: hanoi(1, A, C)

#     hanoi(n-1, A, B)


