def bubble(arr):
    n = len(arr)
    last = 0
    
    while last < n-1:
        ex_per_path = 0 

        for j in range(n-1, last, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                ex_per_path += 1

                # 마지막으로 교환된곳 이전은 이미 정렬된 상태 - 범위 좁히기 
                last = j
        
        # 교환횟수 0 = 정렬완료된 상태
        if ex_per_path == 0:
            break


arr = [5,2,1,4,3,8,6,7]
bubble(arr)
print(arr)
            
            

