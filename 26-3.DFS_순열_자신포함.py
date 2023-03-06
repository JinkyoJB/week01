from typing import List

# path가 aa, ab, ba, bb 즉 경로가 담긴 결과. 최종출력. 
def letter_combination(n):
    def dfs(start_index, path):
        if start_index == n:             # n개를 다 뽑으면 leaf에 도달한 것.
            res.append(''.join(path))
            return
        for letter in ['a', 'b']:
            
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()                   # dfs(1,path)로 재귀를 돌고 나면 수행. 

    res = []
    dfs(0, [])        # 출발점 인덱스를 0, 경로는 빈칸.
    return res


if __name__ == '__main__':
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)

# 왜 letter_combination(2) 로는 출력이 안되지??
# 스택 개념. pop()으로 전부 비워진 후 함수가 끝남.  

# path = ['a','a'] -> res.append(''.join(path)) => 'aa'가 됨!
# path는 그때그때 출력되고, pop()으로 비워짐.
# 만약 하나의 결과에 누적하고 싶으면 index == n로 n개 다 뽑았을 때 
# print하지 않고 res.append(''.join(path)); return 하면 됨. 









# def letter_combination(n):
#     def dfs(start_index, path):
#         if start_index == n:   # n개를 다 뽑으면 leaf에 도달한 것.
#             print(path)
#             return
#         for letter in ['a', 'b']:
#             path.append(letter)
#             dfs(start_index + 1, path)     

#     path = []
#     dfs(0, path)        # 출발점 인덱스를 0, 경로는 빈칸.
#     return path
