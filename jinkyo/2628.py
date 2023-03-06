import sys
import math

input=sys.stdin.readline

a, b = map(int, input().split()) #10 8 
input_num = int(input()) #3 
how_cut_list = [list(map(int, input().split())) for i in range(input_num)] # [[0, 3], [1, 4], [0, 2]]

horizon_list = [0, b]
vertical_list = [0, a]


for i in range(input_num):
    if how_cut_list[i][0]==0: #가로 자르는 거면
        horizon_list.append(how_cut_list[i][1])
    elif how_cut_list[i][0]==1: #세로 자르는 거면
        vertical_list.append(how_cut_list[i][1])

horizon_list.sort()
vertical_list.sort()

hori_list2 = []
vert_list2=[]

for i in range(len(horizon_list)-1):
    inter_h= horizon_list[i+1]-horizon_list[i]
    hori_list2.append(inter_h)

for i in range(len(vertical_list)-1):
    inter_w= vertical_list[i+1]-vertical_list[i]
    vert_list2.append(inter_w)

print(max(hori_list2)*max(vert_list2))






