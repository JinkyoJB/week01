import sys

row, col = map(int,sys.stdin.readline().split())

lines = int(sys.stdin.readline())

cuts = [list(map(int, sys.stdin.readline().split())) for i in range(lines)] 

""" 자르지 않을시 그냥 전체 사각형 넓이, 분기처리 해주지 않으면 20번째 라인에서 indexError """
if len(cuts) == 0:
    print(row*col)

else:
    maxWidth = 0
    widthCuts = []
    maxHeight = 0
    heightCuts = []

    for i in cuts:
        if i[0] == 0: # 수평으로로 자르는
            heightCuts.append(i[1])

        else: # 수직으로 자르는
            widthCuts.append(i[1])

    widthCuts.sort()
    heightCuts.sort()

    """ 자르지 않을시 가로 최대길이는 사각형의 가로와 같음, 분기처리 없으면 indexError발생 """
    if len(widthCuts) == 0:
        maxWidth = row
    else: # 0 ~ widthCuts의 요소들 ~ 맨끝 까지의 파티션 중 가장 긴 값을 선택
        maxWidth = widthCuts[0]
        for i in range(0, len(widthCuts) - 1):
            tmp = widthCuts[i+1]-widthCuts[i]
            maxWidth = max(maxWidth, tmp)
        maxWidth = max(maxWidth ,row - widthCuts[-1])

    """ 세로에도 똑같은 논리 적용 """
    if len(heightCuts) == 0:
        maxHeight = col
    else:
        maxHeight = heightCuts[0]
        for i in range(0, len(heightCuts) - 1):
            tmp = heightCuts[i+1]-heightCuts[i]
            maxHeight = max(maxHeight, tmp)
        maxHeight = max(maxHeight, col - heightCuts[-1])

    print(maxHeight * maxWidth)
