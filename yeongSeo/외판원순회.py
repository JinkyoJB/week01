import sys

n = int(sys.stdin.readline())

visit = [0] * n

path = []
for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    path.append(lst)

def move(now , cnt):
    global charge, ans

    # 이동이 완료됐을시
    if (cnt == n):
        if path[now][0] > 0: # 0이 시작점, 갈 수 있다면 ans 업데이트
            ans = min(ans, charge + path[now][0])
        return
    
    visit[now] = 1
    # now에서 이동할수 있는 도시들 중 
    for i in link[now]: 
        if not visit[i]: # 방문하지 않았다면 
            charge += path[now][i] # 해당도시로의 이동비용 추가
            move(i, cnt+1) # 이동
            charge -= path[now][i] # charge를 계속 사용하므로 이동이 끝났으면 다시 빼줘야함
    
    # now에서의 모든 가능성 체크 후 visit[now]초기화
    visit[now] = 0

link = {}
# 도시간의 이동 가능성 키 -> 리스트 내부 도시 이동가능
for i in range(n):
    link[i] = []
    for j in range(n):
        if path[i][j] > 0:
            link[i].append(j) # 밑과 달리 도시 비용이 아닌 도시 이름으로 이동 가능한지만 체크

charge, ans = 0, sys.maxsize

move(0,1)

print(ans)

"""
딕셔너리에
{
    "도시1" : 도시1비용 도시2비용 도시3비용..
    "도시2" : .....
}

로 비용을 기록

각 도시에서 시작해서 도시로 돌아올수 있는지를 위의 딕셔너리를 활용해서 탐색
"""

import sys

n = int(sys.stdin.readline())

weight = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dic = {}

min_cost = sys.maxsize

# 비용 기록 dictionary 생성 
for i in range(n):
    costs = []
    for j in range(n):
        costs.append(weight[i][j])
    
    dic[i] = costs

visited = [0] * n
def search(start, depth, original, money):
    global min_cost
    visited[start] = 1

    for i in range(n):
        if depth == n and i == original and dic[start][i] != 0:
            min_cost = min(min_cost, money + dic[start][i])
            return

        if dic[start][i] != 0 and visited[i] == 0:
            # visited[i] = 1

            search(i, depth + 1, original, money + dic[start][i])

            visited[i] = 0

for i in range(n):
    search(i, 1, i, 0)

print(min_cost)
