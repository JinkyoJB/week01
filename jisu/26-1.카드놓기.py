def card_combination(k):
    def dfs(start_index, path):     # 카드를 뽑는것도 path임. 
        if start_index == k:
            x = ''.join(map(str, path))
            res.append(x)
            return
        for i in range(len(arr)):
            if used[i] == False:
                used[i] = True
                path.append(arr[i])

                dfs(start_index + 1, path)
                path.pop()
                used[i] = False
    
    res = []
    dfs(0, [])
    return res

# path가 스택이고 res가 출력값

n = int(input())
k = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
used = [False]*len(arr)

res = card_combination(k)

# 중복 없애기
res = list(set(res))
print(len(res))



# if __name__ == '__main__':
#     n = int(input())
#     k = int(input())
#     arr = []
#     for _ in range(n):
#         x = int(input())
#         arr.append(x)
#     used = [False]*len(arr)

#     res = card_combination(k)
#     # 중복 없애기
#     res = set(res)
#     print(count(res))


# 중복 없애기
# set()





# # 1. 입력값 리스트 만들기
# arr = []
# for _ in range(n):
#     x = int(sys.stdin.readline())
#     arr.append(x)

# # 2. k개 뽑기 리스트 함수 만들기 
# res = []

# for i in range(n):
#     a = arr[i]
#     b_list = arr.remove(a)   # a 제외하고 k
#     for b in b_list:
#         if b >= 10:
#             x = a * 100 + b
#             res.append(x)
#         else:
#             x = a * 10 + b
#             res.append(x)

# # 3. 중복 카운트 함수    
# cnt = 0

# def check(k):
#     global cnt
#     for i in range(k+1, len(res), 1):
#         if k == len(res) - 2:
#             return 0
#         if res[k] == res[i]:
#             cnt += 1
#     return cnt + check(k+1)

# check(0)