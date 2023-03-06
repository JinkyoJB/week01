"""
1행 1퀸
각행에 대해 퀸의 가능성 브랜치
각 가지에 대해 자식(한칸 내려간) 디시전스페이스 생성
4 * 4면,  노드의 최대 깊이 4 / 최대 브랜치의 개수 4
TC = n*(n^(n+1)) , 이때 n곱하는 이유는 행(n)을 선형으로 보며 퀸이 놓일수 있는지 체크하기 때문 
이때 O(n)을 O(1)으로 줄일 수 있다.
1. 행겹치는지 체크 안해도 됨(행 별로 노드를 내려가기 때문)
2. 열에대한 체크 : HashSet안에 앞선(위 행)들의 퀸의 열 위치 기록 - 겹치는지 확인 
3. 대각선 : 마찬가지로 HashSet활용, 같은 왼쪽 대각선에 있으면 x-y의 값이 같음, 이를 hashSet에 넣음 / 
    같은 오른쪽 대각선의 경우 x+y의 값이 같음. 마찬가지로 hashSet에 넣어서 O(1)으로 검증
"""
import sys

n = int(sys.stdin.readline())

cases = 0

dRow = [-1] * n # 인덱스값 : 열, 인덱스 안의 값: 행 => 한열당 하나의 퀸만 올 수 있기에 이런 구조 가능

def queen(cnt):
    global cases

    for i in range(n):
        if is_promising(i, cnt): #cnt행의 i자리에 퀸을 놓을 수 있는지 체크
            if cnt == n-1:
                cases += 1
                return 
            
            dRow[i] = cnt

            queen(cnt + 1)

            dRow[i] = -1
        

def is_promising(i, cnt): # cnt행 i열
    if dRow[i] != -1:
        return False

    # 대각선 체크 
    for j in range(n):
        if dRow[j] != -1:
            if abs(cnt - dRow[j]) == abs(i - j):
                return False 
    
    return True

queen(0)

print(cases)


""" 1d array가 아니면? 
TC = n^2 * (n^(n+1))
시간초과
""" 
import sys

n = int(sys.stdin.readline())

cases = 0

dRow = [[0] * n for _ in range(n)]

def queen(row):
    global cases

    for i in range(n):
        if is_promising(row, i): 
            if row == n-1:
                cases += 1
                return 
            
            dRow[row][i] = 1

            queen(row + 1)

            dRow[row][i] = 0
        

def is_promising(row, col): 
    #열 체크 - 1d 사용시 해당 열에 값이 존재하는지만 확인했던것(O(1))과 달리 O(n),
    for i in range(n):
        if dRow[i][col] != 0:
            return False

    # 대각선 체크 - 1d와 달리 O(n^2) 
    for i in range(n):
        for j in range(n):
            if i - j == row - col or i + j == row + col:
                if dRow[i][j] != 0:
                    return False
    
    return True

queen(0)

print(cases)
