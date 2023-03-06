import sys

def selection(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        tmp_min = sys.maxsize

        for i in range(start, end):
            if arr[i] < tmp_min:
                tmp_min = arr[i]
        