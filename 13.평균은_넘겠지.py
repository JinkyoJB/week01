n = int(input())

for _ in range(0, n, 1):
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]       # 정수끼리 비교
    cnt = 0

    for num in score[1:]:
        if num > avg:
            cnt += 1
    rate = cnt / score[0] * 100
    print(f'{rate:.3f}%')


# map(함수, 리스트명): 리스트 요소들을 함수로 매핑
# format 넣는 건 마지막 print에. list에 append할 때는 raw로. 
# for num in A -> 비교 시 A[i] 말고 num 써야 함. 


# C = int(input())

# res = []

# for _ in range(0, C, 1):
#     inputList = input().split()
#     inputList = list(map(int, inputList))

#     N = inputList[0]
#     score = inputList[1:]

#     cnt = 0;
#     avg = sum(score) / len(score);

#     for i in range(0, N, 1):
#         if score[i] > avg:
#             cnt += 1;

#     rate = (cnt / N) * 100
#     res.append(rate)


# for i in range(0, C, 1):
#     print(round(res[i],3)+'%')




