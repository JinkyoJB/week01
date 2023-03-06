
# 왜 s1, s2에 path가 담기지??
# 매개변수 늘리기: 'int' object is not iterable / return을 해줘야 cnt에 반영됨. 
def hanoi(N, from_loc, to_loc, mid_loc, path=[]):
    if N == 1:
        x = str(from_loc)+str(to_loc)
        path.append(x)
        return 1                     
    else:
        s1 = hanoi(N-1, from_loc, mid_loc, to_loc, path)

        x = str(from_loc)+str(to_loc)
        path.append(x)
        
        s2 = hanoi(N-1, mid_loc, to_loc, from_loc, path)
        
        return s1 + s2 + 1
        # for i in path:
        #     print(i)

hanoi(3, 1, 3, 2, [])

# for i in __path__:
#     print(i)



# n만 받으면 들어오게끔
# def makeHanoi(n):
#     def hanoi(N, from_loc, to_loc, mid_loc, cnt, path):
#         if N == 1:
#             path.append(f'{from_loc} {to_loc}')
#             cnt += 1
#         else:
#             hanoi(N-1, from_loc, mid_loc, cnt, path)
#             path.append(f'{from_loc} {to_loc}')
#             hanoi(N-1, mid_loc, to_loc, cnt, path)
#             cnt += 1

#     hanoi(n, 1, 3, 2, 0, [])




# 매개변수에 cnt = 0을 넣어버리면 재귀 돌 때마다 초기화됨.. 
# def hanoi(N, from_loc, to_loc, mid_loc, cnt, path=[]):
#     if N == 1:
#         path.append(f'{from_loc} {to_loc}')
#         cnt += 1
#         return cnt                     
#     else:
#         s1 = hanoi(N-1, from_loc, mid_loc, to_loc, cnt, path)
#         path.append(f'{from_loc} {to_loc}')
#         cnt += 1
#         s2 = hanoi(N-1, mid_loc, to_loc, from_loc, cnt, path)
        
#         return s1 + s2

# hanoi(3, '1', '3', '2', 0, [])
# # for i in __path__:
# #     print(i)


# 매개변수 늘리기: 'int' object is not iterable / return을 해줘야 cnt에 반영됨. 
# def hanoi(N, from_loc, to_loc, mid_loc, path=[]):
#     if N == 1:
#         x = str(from_loc)+str(to_loc)
#         path.append(x)
#         return 1                     
#     else:
#         s1 = hanoi(N-1, from_loc, mid_loc, to_loc, path)
#         x = str(from_loc)+str(to_loc)
#         path.append(x)
#         s2 = hanoi(N-1, mid_loc, to_loc, from_loc, path)
#         print(s1 + s2 + 1)
#         for i in path:
#             print(i)

# hanoi(3, 1, 3, 2, [])