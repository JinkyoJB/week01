arr = [1,2,3,4,5]
used = [False]*len(arr)

print(used)

def perm(res, n):
    if n == 0:
        print(res)
        return
    for i in range(len(arr)):       # i는 매번 0번째부터 반복. n만 -1씩 깎을 뿐.
        if used[i] == False:        # used가 0이면 (아직 안뽑은 숫자)
            used[i] = True
            res.append(arr[i])

            perm(res, n-1)

            res.pop()               # pop()도 재귀함수 중 하나. perm(res, n=1)일 때 pop 한번, 빠져나와서 perm(res, n=2)일 때 pop 한번. 이렇게 두 카드 모두 비워짐.
            used[i] = False

perm([], 2)



# used는 몇번째 숫자를 지금 arr에서 포함했는지 확인하기위한 칼럼.
# False, True를 0, 1로 바꿔보기. 



# arr = [1,2,3,4,5]
# used = [0]*len(arr)

# print(used)

# def perm(res, n):
#     if n == 0:
#         print(res)
#         return
#     for i in range(len(arr)):      
#         if not used[i]:            
#             used[i] = 1
#             res.append(arr[i])

#             perm(res, n-1)

#             res.pop()
#             used[i] = 0

# perm([], 2)
