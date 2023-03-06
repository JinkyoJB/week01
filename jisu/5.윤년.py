x = int(input())

if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
    print(1)
else:
    print(0)


# 추가
# 조건문을 하나의 변수로 담아서 
# if A and (B or C)로 표현하는 법