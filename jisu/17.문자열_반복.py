T = int(input())

for i in range(0, T, 1):
    R, string = input().split()
    R = int(R)
    arr = list(str(string))   # str에 또 str 넣으면 오류나나?

    for i in range(0, len(arr), 1):
        for j in range(0, R, 1):
            print(arr[i], end="")
    print("")

# input을 두 번 받는 경우, 한 번 결과가 나오면 print("")로 한 줄 띄워준다.